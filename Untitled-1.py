import requests 
from bs4 import BeautifulSoup 
import sys
sys.stdout=open("test.txt","w")

url="	https://insights.blackcoffer.com/will-machine-replace-the-human-in-the-future-of-work/"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'}

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')
s    = soup.find('div', id ="td-outer-wrap")

for line in soup.find_all('p'):
	print(line.text)
sys.stdout.close()