import socket

host = 'localhost'

mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# SOCK_STREAM means TCP
addr=(host,5555)
mysock.connect(addr)

try:
    msg = b'hi,this is a test\n'
    mysock.sendall(msg)
except socket.errno as e:
    print('socket error',)
finally:
    mysock.close()
