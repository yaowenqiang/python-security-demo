import socket
mgrp = '224.1.1.1'
mgport = 5775
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
for i in range(1,10):
    sock.sendto(b'Hi,this is me.',(mgrp,mgport))

print('Message send out to the multicast group')
