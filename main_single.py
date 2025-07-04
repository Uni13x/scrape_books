import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

url = "https://books.toscrape.com/"
res = requests.get(url)
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'lxml')

books = soup.select('article.product_pod')

data = []
for book in books:
  title = book.h3.a.get('title')
  price = book.select_one('.price_color').text
  availability = book.select_one('.availability').text.strip()
  data.append({
    'Title': title,
    'Price': price,
    'Availability': availability
  })
  
  time.sleep(2)
  
df = pd.DataFrame(data)
df.to_csv('sample_output.csv', index=False, encoding='UTF-8')

