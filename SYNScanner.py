from scapy.all import *
from threading import Thread
from tqdm import tqdm

target_ip = input("Please enter an ip: ")
threads = 50

def syn_scan(target_ip,port):
    src_port = RandShort()
    packet = sr1(IP(dst=target_ip)/TCP(sport=src_port, dport=port, flags="S"),verbose=0)
    if packet[TCP].flags == 18:
        print(f"Port {port} is open")

all_threads = []
ports = range(1, 65535)


for port in ports:
	thread = Thread(target=syn_scan, args=(target_ip,port))
	thread.daemon = True
	thread.start()
	all_threads.append(thread)

print("All ports have been scanned")
