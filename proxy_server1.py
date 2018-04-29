import socket
import threading
import signal
import sys

config = {
			"HOST_NAME" :"192.168.0.114",
			"BIND_PORT": 12346,
			"MAX_REQUEST_LEN" : 4096,
            "CONNECTION_TIMEOUT" : 10
	
		}

class Server:
    """ The server class """
    #PART1: Creating a socket for the server
    #We will now do it in a function
    #and to listene to a max of 10 clients at a time

    def __init__(self, config):
        signal.signal(signal.SIGINT, self.shutdown)     # Shutdown on Ctrl+C
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)             # Create a TCP socket
        self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)    # Re-use the socket
        self.serverSocket.bind((config['HOST_NAME'], config['BIND_PORT'])) # bind the socket to a public host, and a port
        self.serverSocket.listen(10)    # become a server socket
        self.__clients = {}


    def listen_for_client(self):
        """ Wait for clients to connect """
        #PART 2:LISTEN FOR CLIENT We wait for the clients connection request and once a
        #successful connection is made we dispatch the request in a separate thread,
        #making ourselves available for the next request.
        #This allows us to handle multiple requests simultaneously which boosts the performance of the 
        #server multifold times. -> we need a function for threading and to get client name!!!


        while True:
            (clientSocket, client_address) = self.serverSocket.accept()   # Establish the connection
            d = threading.Thread(name=self._getClientName(client_address), target=self.proxy_thread, args=(clientSocket, client_address))
            d.setDaemon(True)
            d.start()
        self.shutdown(0,0)


    def proxy_thread(self, conn, client_addr):
        
        #NOTE guys : SYS module -> ssize_t recv(int sockfd, **** void *buf ***** (we use only this), size_t len, int flags); => this is a simple linux function

        #PART1: get the request from the client 
        # parse the url to get info on webserver , the port
        # if no port is specifies use the default 80

        request = conn.recv(config['MAX_REQUEST_LEN'])        # get the request from browser
        first_line = request.split('\n')[0]                   # parse the first line
        url = first_line.split(' ')[1]                        # get url

        #print(url)                       

        # find the webserver and port
        http_pos = url.find("://")  # find pos of ://

        #print(http_pos) 

        if (http_pos==-1):
            temp = url
        else:
            temp = url[(http_pos+3):]       # get the rest of url
            #print("reqd_url:",temp)

        port_pos = temp.find(":")           # find the port pos (if any) =>returns -1 if none found
        #print("port_pos:",port_pos)

        # find end of web server=> if / not found it is just set as length of the reqd_url
        webserver_pos = temp.find("/")
        if webserver_pos == -1:
            webserver_pos = len(temp)

        webserver = ""
        port = -1

        if (port_pos==-1 or webserver_pos < port_pos):      # default port
            port = 80
            webserver = temp[:webserver_pos]
        else:                                               # specific port
            port = int((temp[(port_pos+1):])[:webserver_pos-port_pos-1])
            webserver = temp[:port_pos]

        print("Final_web_server:",webserver,"Port:",port)


        

        try:
            # create a socket to connect to the web server
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #s.settimeout(config['CONNECTION_TIMEOUT'])
            s.connect((webserver, port))                 #connecting to the server using url and port
            s.sendall(request)                           # send request to webserver

            while 1:
                data = s.recv(config['MAX_REQUEST_LEN'])    # receive data from web server as reply to request
                #print(data)          
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


