# Book Scraper (Books to Scrape)

## 内容/Description

このリポジトリには、以下の2種類のスクレイピングスクリプトが含まれています。
This repository contains two types of scraping scripts:

main_single.py：1ページ分だけをスクレイピングするシンプル版
main_single.py: A simple version that scrapes a single page

main.py：全ページを巡回してデータを取得する完全版
main.py: A complete version that crawls all pages and extracts data

このスクリプトは books.toscrape.com から書籍情報（タイトル、価格、在庫）を取得し、CSV形式で保存します。
The script scrapes book data (title, price, availability) from books.toscrape.com and saves it as a CSV file.

## 使用技術 / Technologies Used
Python 3.12

requests

BeautifulSoup4

lxml

pandas

time（標準ライブラリ / standard library）

## ▶ 使い方 / How to Use
1．必要なライブラリをインストール
Install required libraries : pip install requests beautifulsoup4 lxml pandas

2.スクリプトを実行
Run the script : python main.py

3.sample_output.csv が生成されます。
The file sample_output.csv will be generated.

## 出力例 / Example Output

Title,Price,Availability
A Light in the Attic,£51.77,In stock
Tipping the Velvet,£53.74,In stock

## ⚠ 注意点 / Notes
サーバーへの負荷を避けるため、リクエスト間に time.sleep(2) を入れています。
To avoid server overload, a time.sleep(2) delay is added between requests.

商用利用ではなく学習目的のみに使用してください。
For educational use only. Not intended for commercial use.