from scapy.all import *
from  multiprocessing import Pool, cpu_count

host = input("please enter an ip Address: ")
port = (1,65535)
def syn(port):
	for port in range(port):
		ans = sr1(IP(dst=host)/TCP(dport=(port),flags="S"),verbose=0)
		if int(ans[TCP].flags) == 18:
			print (port)


num_cpu = max(1,cpu_count() - 1)
with Pool(num_cpu) as mp_pool:
	mp_pool.map(syn,port)


