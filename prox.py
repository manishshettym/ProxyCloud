import socket
import threading
import signal
import sys


config =  {
            "HOST_NAME" : "127.0.0.1",
            "BIND_PORT" : 12345,
            "MAX_REQUEST_LEN" : 1024,
            "CONNECTION_TIMEOUT" : 5
          }






class Server:
    """ The server class """
    
    #PART1: Creating a socket for the server
    #We will now do it in a function
    #and to listene to a max of 10 clients at a time 

    def __init__(self, config):
        # Shutdown on Ctrl+C
        signal.signal(signal.SIGINT, self.shutdown) 

        # Create a TCP socket
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Re-use the socket
        self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # bind the socket to a public host, and a port   
        self.serverSocket.bind((config['HOST_NAME'], config['BIND_PORT']))
        
        self.serverSocket.listen(10) # become a server socket
        self.__clients = {}



    def listen_for_client(self):


        #PART 2:LISTEN FOR CLIENT We wait for the clients connection request and once a
        #successful connection is made we dispatch the request in a separate thread,
        #making ourselves available for the next request.
        #This allows us to handle multiple requests simultaneously which boosts the performance of the 
        #server multifold times. -> we need a function for threading and to get client name!!!

        while True:
        
            # Establish the connection
            (clientSocket, client_address) = self.serverSocket.accept() 
            
            #note we used to send the messages from the server in the same  request 
            # now using a different thread we can make ourselves available for other requests

            d = threading.Thread(name=self._getClientName(client_address), 
            target = self.proxy_thread, args=(clientSocket, client_address))
            d.setDaemon(True)
            d.start()
        

    #This function will create a thread to handle request from a client:
    def proxy_thread(self, conn, client_addr):


        #NOTE guys : SYS module -> ssize_t recv(int sockfd, **** void *buf ***** (we use only this), size_t len, int flags); => this is a simple linux function

        #PART1: get the request from the client 
        # parse the url to get info on webserver , the port
        # if no port is specifies use the default 80
        request = conn.recv(config['MAX_REQUEST_LEN'])        # get the request from browser
        first_line = request.split('\n')[0]                   # parse the first line
        url = first_line.split(' ')[1]                        # get url

        # find the webserver and port
        http_pos = url.find("://")          # find pos of :// because what comes after this is the intersting part
        if (http_pos==-1):                  # nothing present
            temp = url
        else:
            temp = url[(http_pos+3):]       # get the rest of url -> +3 because :// are 3 characters from pos 
                                            # and we need  from there on to the ends

        port_pos = temp.find(":")           # find the port pos (if any)


        webserver_pos = temp.find("/")      # find the end of the webserver
        if webserver_pos == -1:
            webserver_pos = len(temp)

        webserver = ""
        port = -1
        if (port_pos==-1 or webserver_pos < port_pos):      # default port if not provided
            port = 80
            webserver = temp[:webserver_pos]
        else:                                               # specific port if was provided in the url
            port = int((temp[(port_pos+1):])[:webserver_pos-port_pos-1])
            webserver = temp[:port_pos]


        try:
            # create a socket to connect to the web server
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(config['CONNECTION_TIMEOUT'])
            s.connect((webserver, port))
            s.sendall(request)                           # send request to webserver

            while 1:
                data = s.recv(config['MAX_REQUEST_LEN'])          # receive data from web server
                if (len(data) > 0):
                    conn.send(data)                               # send to browser
                else:
                    break
            s.close()
            conn.close()
        except socket.error as error_msg:
            print 'ERROR: ',client_addr,error_msg
            if s:
                s.close()
            if conn:
                conn.close()

    def _getClientName(self, cli_addr):
        """ Return the clientName.
        """
        return "Client"


    def shutdown(self, signum, frame):
        """ Handle the exiting server. Clean all traces """
        self.serverSocket.close()
        sys.exit(0)


if __name__ == "__main__":
    server = Server(config)
    server.listen_for_client()
