import urllib2
import urllib

url = 'http://192.168.1.111/test.php'
data = {'name':'Ric','age':'30','btnSubmit':'submit'}
params = urllib.urlencode(data)
req = urllib2.Request(url,data=params)
handle = urllib2.urlopen(req)
page = handle.read()
print(page)
