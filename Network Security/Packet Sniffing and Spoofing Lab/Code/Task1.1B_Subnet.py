#!/usr/bin/env python3
from scapy.all import *
print("SNIFFING PACKET...")
def print_pkt(pkt):
	pkt.show()
pkt = sniff(iface="br-58b8bb656edb", filter="src net 172.17.0.0/24", prn=print_pkt)
