import urllib2
proxy = urllib2.ProxyHandler({'http':'127.0.0.1:8000'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)
handle = urllib2.urlopen('http://www.baidu.com')
print(handle.readOP)
