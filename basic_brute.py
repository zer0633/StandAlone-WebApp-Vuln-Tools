mport requests
import sys

target = "http://testphp.vulnweb.com/"
wordlist = '/home/heretic-haxxor/wordlists/SecLists/Discovery/Web-Content/raft-small-directories.txt'

word = open(wordlist,'r')
for file in word:
        file.strip()
        url = target+file.strip()
        r = requests.get(url)
        if r.status_code == 200:
                print(f'\n {url} {r.status_code}')
        else:
                sys.stderr.write('.');sys.stderr.flush()

