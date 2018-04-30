import BaseHTTPServer
import hashlib
import os
import urllib2
import random

#PROXY STACK
proxies = []
proxies.append({
        'ip':"192.168.0.114",
        'port':"12345" 
        })

proxies.append({
        'ip':"192.168.0.114",
        'port':"12346" 
        })

request_count = 0



class CacheHandler(BaseHTTPServer.BaseHTTPRequestHandler):


    def do_GET(self):

      



      m = hashlib.md5()
      m.update(self.path),
      cache_filename = m.hexdigest()

      req_c = counterincrement();

      print("THE REQ COUNT IS : ",req_c)

      print("<-----:",cache_filename,":------>");

      if os.path.exists("/home/manish/ACADEMICS/PROJECTS/ProxyCloud/cache/"+cache_filename):
          print "Cache hit"
          data = open("/home/manish/ACADEMICS/PROJECTS/ProxyCloud/cache/"+cache_filename).readlines()
          
         #if a hit then no need for any proxies to work -> LET THEM REST lol:P
         
      
      else:
          print "Cache miss"
          #data = urllib2.urlopen(self.path).readlines()

          # Every 10 requests, generate a new proxy
          if req_c % 2 == 1:
            proxy_index = 0
            proxy = proxies[proxy_index]

          elif req_c % 2 == 0:
            proxy_index = 1
            proxy = proxies[proxy_index]

          req = urllib2.Request(self.path )
          req.set_proxy(proxy['ip'] + ':' + proxy['port'], 'http')
          
          print(req)
          data = urllib2.urlopen(req)
          #req = urllib2.Request(self.path)
          open("/home/manish/ACADEMICS/PROJECTS/ProxyCloud/cache/"+cache_filename, 'wb').writelines(data)


      self.send_response(200)
      self.end_headers()
      self.wfile.writelines(data)

def counterincrement():
  global request_count
  request_count+=1
  return request_count


def run():
    server_address = ("192.168.0.114", 1025)
    httpd = BaseHTTPServer.HTTPServer(server_address, CacheHandler)
    httpd.serve_forever()

if __name__ == "__main__":
    run()

