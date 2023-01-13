from scapy.all import *
from threading import Thread

host = input("Please enter an ip: ")
threads = 50

def syn_scan(host,port):
    src_port = RandShort()
    packet = sr1(IP(dst=host)/TCP(sport=src_port, dport=port, flags="S"),verbose=0)
    if packet[TCP].flags == 18:
        print(f"Port {port} is open")

all_threads = []
ports = deque(range(1, 65535))


max_threads = 100
while ports:
    for i in range(max_threads):
        if ports:
            port = ports.popleft()
            thread = Thread(target=syn_scan, args=(host,port))
            thread.daemon = True
            thread.start()
            all_threads.append(thread)
    for thread in all_threads:
        thread.join()
    all_threads = []
print("All ports have been scanned")
