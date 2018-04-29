import urllib2
import random

proxies = [] # Will contain proxies [ip, port]

# Main function
def main():
  # Retrieve proxies and store into a dictionary
  
  proxies.append({
              'ip':"localhost",
              'port':"12345" 
              })

  '''proxies[1]={
              'ip':" ",
              'port':" " 
              }'''


  # Choose a random proxy
  #proxy_index = random_proxy()
  #proxy = proxies[proxy_index]

  proxy = proxies[0]

  for n in range(1, 2):
    req = urllib2.Request('http://www.espncricinfo.com')
    req.set_proxy(proxy['ip'] + ':' + proxy['port'], 'http')

    # Every 10 requests, generate a new proxy
    '''if n % 10 == 0:
      proxy_index = random_proxy()
      proxy = proxies[proxy_index]'''

    data = urllib2.urlopen(req).read().decode('utf8')
    print('#' + str(n) + ': ' + data)
  

# Retrieve a random index proxy (we need the index to delete it if not working)
def random_proxy():
  print(len(proxies))
  return random.randint(0, len(proxies)-1)

if __name__ == '__main__':
  main()
