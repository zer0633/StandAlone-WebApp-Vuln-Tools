import socket
from threading import Thread
from collections import deque
host = input("Please enter an ip: ")
threads = 50

def syn_scan(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        try:
            s.connect((host, port))
            print(f"Port {port} is open")
        except socket.timeout:
            pass

all_threads = []
ports = deque(range(1, 65535))

# Add a maximum number of threads
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

