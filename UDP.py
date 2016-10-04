import socket
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(b'Hi,this is a message', ('172.30.42.112',5599))
except Exception as e:
    print('Exception: ',e)
finally:
    print('Send the message')
