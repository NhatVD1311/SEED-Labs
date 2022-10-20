#!/usr/bin/env python3
from scapy.all import *
print("SENDING SPOOFED ICMP PACKET...")


IPLayer = IP()
IPLayer.src = "10.9.0.11" 
IPLayer.dst = "10.9.0.55" 

ICMPpkt = ICMP()
pkt = IPLayer/ICMPpkt
pkt.show()
send(pkt)
