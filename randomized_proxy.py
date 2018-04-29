import random
import urllib2

# put the urls for all of your proxies in a list
proxies = ['http://localhost:12345/']

# construct your list of url openers which each use a different proxy
openers = []
for proxy in proxies:
    opener = urllib2.build_opener(urllib2.ProxyHandler({'http': proxy}))
    openers.append(opener)

# select a url opener randomly, round-robin, or with some other scheme
opener = random.choice(openers)
req = urllib2.Request("http://www.espncricinfo.com")
res = opener.open(req)