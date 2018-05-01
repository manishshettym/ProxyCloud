# ProxyCloud
A simple locally hosted  multiproxy caching server system created in python and it's vast set of modules for LANs.
The webserver deployed is a simple BaseHttp Server written in python with caching abilities.
The proxy servers ( right now only 2 , but can be exemplified with more) are po



### Running the project

**1.Point your browsers proxy to the WebServers IP and port

**2.To run the webserver:

```sh
cd /path/to/your/directory
python threading_cache_proxy.py
```
**3.To run the two proxies built in:

```sh
cd /path/to/your/directory
python proxy_server<serverid>.py
```

**4.To run the website:
```sh
cd /path/to/your/directory
python3 app2.py
```


## Uses

