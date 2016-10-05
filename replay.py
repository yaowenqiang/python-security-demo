from scapy.all import *
from scapy.utils import rdpcap
src_mac=''
dst_mac=''
src_ip = ''
dst_ip = ''

frames = rdpcap('file.pcap') # could alswo read in only a small number of packets
for frame in frames:
    try:
        frame[Ether].src = src_mac
        frame[Ether].dst = dst_mac
        if IP in frame:
            frame[IP].src = src_ip
            frame[IP].dst = dst_ip
        sednp(frame)
    except Exception as e:
        print(e)


