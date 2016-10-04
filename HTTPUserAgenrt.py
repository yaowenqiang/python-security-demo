import httplib

h = 'localhost'

req = httplib.HTTP(h)
req.putrequest('GET','/index.html')
req.putheader('Host',h)
req.putheader('User-Agent','Garbage browser: 5.6')
req.endheaders()
req.send('')

statusCode,statusMsg,headers = req.getreply()
print('Response Code: ',statusCode)
print('Response: Msg ',statusMsg)
for header in headers:
    print(header)
