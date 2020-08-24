import requests
from bs4 import BeautifulSoup

Caterpillarpage = requests.get('https://www.marketwatch.com/investing/stock/cat')
Catsoup = BeautifulSoup(Caterpillarpage.content, 'html.parser')
print(Catsoup)