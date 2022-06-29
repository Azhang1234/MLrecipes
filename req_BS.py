from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import sys 

stdoutOrigin=sys.stdout 
sys.stdout = open("log.txt", "w")


url = "http://books.toscrape.com/"
req = requests.get(url)
content = req.text

soup=BeautifulSoup(content, 'html.parser')
print(soup.prettify())


setList = []
for i in soup.find_all(class_='product_price'):
  setList.append([x[0] for x in re.findall('([0-9]+(\.[0-9]+)?)', i.text)])
print(setList)

sys.stdout.close()
sys.stdout=stdoutOrigin

'''brand_name = []
price = []
location = []
description = []
rating_score = []
raw = soup.findAll('script')[3].text
page = pd.read_json(raw.split("window.pageData=")[1],orient='records')
for item in page.loc['listItems','mods']:
    brand_name.append(item['brandName'])
    price.append(item['price'])
    location.append(item['location'])
    description.append(ifnull(item['description'],0))
    rating_score.append(ifnull(item['ratingScore'],0))
output=pd.DataFrame({'brandName':brand_name,'price':price,'location':location,'description':description,'rating score':rating_score})
output.to_csv('output.csv',index=False)'''