import urllib.request
import random
from random import randint
import time
import sys

def RandomLove():
	url= "http://www.nowcheerup.me/index.php"
	randNumber = [random.choice(['6', '7'])] + [str(random.randint(0,9)) for r in range(8)]
	data = "number=%2B33"+"".join(randNumber)+"&submit=Cheer Up Time!"
	print("Number 0"+"".join(randNumber)+" cheered up :) ")
	if sys.version_info >= (3,0):
		data = data.encode('UTF-8')
	req = urllib.request.Request(url, data)
	response = urllib.request.urlopen(req)
	page = response.read()
	print("OK" if "success.png" in page.decode() else "Not OK")
	

while(1):
	RandomLove()
	time.sleep(60)
