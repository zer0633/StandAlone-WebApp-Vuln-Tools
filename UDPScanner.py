from scapy.all import *
from threading import Thread
import time

host = input("please enter an ip Address: ")
threads = 10


def udpscan(host,port):
	src_port = RandShort()
	ans, unans = sr(IP(dst=host)/UDP(sport=src_port, dport=port),verbose=0,timeout=2)
	for sent,received in ans:
		if received.haslayer(UDP) and received[UDP].sport==port:
			print(f"Port {port} is open")

all_threads = []
ports = range(1,65535)

for port in ports:
	thread = Thread(target=udpscan, args=(host,port))
	thread.start()
	all_threads.append(thread)


print("All ports have been scanned")
