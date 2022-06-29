import bs4
import requests
from bs4 import BeautifulSoup
import re
r = requests.get('https://finance.yahoo.com/lookup')

content = r.text

soup=BeautifulSoup(content, 'html.parser')

setList = []
for i in soup.find_all(class_='data-col2 Ta(end) Pstart(20px)'):
  setList.append([x[0] for x in re.findall('([0-9]+(\.[0-9]+)?)', i.text)])
print(setList)
#found the price of the trending stocks!