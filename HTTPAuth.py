import httplib
import base64
import string

h = 'localhost'
u = 'username'
p = 'password'

authToken = base64.encodestring('{}:{}'.format(u,p)).replace('\n','')

print(authToken)

req = httplib.HTTP(h)
req.putrequest('GET','/index.html')
req.putheader('Host',h)
req.putheader('Authorization','Basic {}'.format(authToken))
req.endheaders()
req.send('')

statusCode,statusMsg,headers = req.getreply()
print('Response Code: ',statusCode)
print('Response: Msg ',statusMsg)
for header in headers:
    print(header)
