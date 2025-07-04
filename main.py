import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

base_url = "https://books.toscrape.com/catalogue/page-{}.html"
page = 1
data = []

while True:
  url = base_url.format(page)
  print(f"scraping page {page}: {url}")
  
  r = requests.get(url)
  r.encoding = "UTF-8"
  time.sleep(2)
  
  if r.status_code != 200:
    print("終了：これ以上ページがないか、エラー")
    break
  
  soup = BeautifulSoup(r.text, "lxml")
  
  books = soup.select("article.product_pod")
  if not books:
    print("終了：データが見つからなかったため")
    break
  
  for book in books:
    title = book.h3.a["title"]
    price = book.select_one('.price_color').text
    availability = book.select_one(".availability").text.strip()
    data.append({
      "Title": title,
      "price": price,
      "availability": availability
    })
  
  page += 1
  time.sleep(2)

df = pd.DataFrame(data)
df.to_csv("sample_all_output.csv", index=False, encoding="UTF-8")
