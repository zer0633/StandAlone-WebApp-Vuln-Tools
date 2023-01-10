from scapy.all import *
from  multiprocessing import Pool, cpu_count
import time
host = input("please enter an ip Address: ")
port = (1,65535)
def udpscan(port):
	for port in range(port):
		ans = sr1(IP(dst=host)/UDP(dport=port),verbose =0)
		time.sleep(0.7)
		if ans == None:
			print (port)
		else:
			print(port)

num_cpu = max(1,cpu_count() - 1)
with Pool(num_cpu) as mp_pool:
        mp_pool.map(udpscan,port)
