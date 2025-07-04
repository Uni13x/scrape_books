# Book Scraper (Books to Scrape)

このスクリプトは [books.toscrape.com](https://books.toscrape.com/) から書籍情報（タイトル、価格、在庫）を取得し、CSV形式で保存します。

## 使用技術

- Python 3.x
- requests
- BeautifulSoup4
- lxml
- time（標準ライブラリ）

## 使い方

1. 必要なライブラリをインストール
2. スクリプトを実行
3. `sample_output.csv` が生成されます。

## 出力例
Title,Price,Availability
A Light in the Attic,£51.77,In stock
Tipping the Velvet,£53.74,In stock

## 注意点
- サーバーへの負荷を避けるため、リクエスト間に `time.sleep(2)` を入れています。
- 商用利用ではなく学習目的のみに使用してください。