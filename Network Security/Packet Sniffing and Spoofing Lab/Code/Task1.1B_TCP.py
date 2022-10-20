#!/usr/bin/env python3
from scapy.all import *
print("SNIFFING PACKET...")
def print_pkt(pkt):
	pkt.show()
pkt = sniff(iface="br-58b8bb656edb", filter="tcp and src host 10.9.0.5 and dst port 23", prn=print_pkt)
