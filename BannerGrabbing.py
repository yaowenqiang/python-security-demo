import socket
import re
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('www.microsoft.com',80))

http_get = b'GET / HTTP/1.1\nHost: www.microsoft.com\n\n'
data = ''
try:
    sock.sendall(http_get)
    data = sock.recvfrom(1024)
except socket.error:
    print('Socket error',socket.errno)
finally:
    print('Closing connection')
    sock.close()

strdata = data[0].decode('utf-8')

# Looks like one line line so split it at newline into multiple strings
headers = strdata.splitlines()
# use regular expression library to llo for the one line we like
for s in headers:
    if re.search('Server:',s):
        s = s.replace('Server:','')
        print(s)

    #print(s)


