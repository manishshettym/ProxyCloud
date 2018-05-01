![alt text](https://github.com/ManishShettyM/ProxyCloud/blob/master/WebApp.png)


# ProxyCloud
- A simple locally hosted  multiproxy caching server system created in python and it's vast set of modules for LANs.

- The webserver deployed is a simple BaseHttp Server written in python with caching abilities.
- The proxy servers ( right now only 2 , but can be exemplified with more) are chosen on  [Round-Robin] Algorithmic order
  to implement load balancing to the webserver's request




### Running the project

* Point your browsers proxy to the WebServers IP and port

* To run the webserver:

```sh
cd /path/to/your/directory
python threading_cache_proxy.py
```
* To run the two proxies built in:

```sh
cd /path/to/your/directory
python proxy_server<serverid>.py
```

* To run the proxy Web-App:
```sh
cd /path/to/your/directory
python3 app2.py
```
## Development

* Build and Add more proxies for your server with a few lines of simple code
* Apply better caching techniques and load-balancing methods


## Tech/Libraries/Modules used
* [Flask] - A micro web framework written in Python and based on the Werkzeug toolkit and Jinja2 template engine. (Web App)
* [Urllib2] - Urllib2 module defines functions and classes which help in opening URLs (mostly HTTP)
* [Hashlib] - A hashing library used to hash cached services of webpages that makes retrieving easier
* [Socket] - A socket programming module that allows creating sockets for servers for connections following TCP
* [Threading] - A module to run parallel executions speeding up the request process




