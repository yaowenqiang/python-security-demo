import socket

size = 512
host = ''
port = 9898

# family = Internet,type = STREAM  SOCKET MEANS tcp sock = socket.socket()
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

# we have a socket,we need to bind to an IP address and port
# to have a place to listen to

sock.bind((host,port))
sock.listen(5)

# we can stor information about the other end
# once we accept the connection attempt

c,addr = sock.accept()
data = c.recv(size)

if data:
    f = open('storage.dat','+w')
    print('connection from :',addr[0])
    f.write(addr[0])
    f.write(':')
    f.write(data.decode('utf-8'))
    f.close()
sock.close()
