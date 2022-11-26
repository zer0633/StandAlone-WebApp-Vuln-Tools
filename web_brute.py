
"""imports used to create requests and threading"""
import threading
import concurrent.futures
import requests
import time

"""variables for webpage and wordlist"""
t = input("please enter a webpage: ")
wordlist = input("please enter a wordlist: ")

"""open wordlist and turn into a list instead of a string once string has been made close wordlist"""
with open(wordlist) as f:
	word = [word.strip() for word in f]
	f.close()

"""defining the target and request status and printing"""
def words(word):
	target  = t + word	
	r = requests.get(target)
	if r.status_code < 400:
		print(f'{target} {r.status_code}')


"""creating thread pool exeuctor for executor.map for threads"""
with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
	executor.map(words,word)
