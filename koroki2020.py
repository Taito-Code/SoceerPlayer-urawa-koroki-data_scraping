from bs4 import BeautifulSoup
import pandas as pd
import requests
import csv

# 興梠選手のデータURL
url = "https://www.football-lab.jp/player/500165/"

# URLからHTMLを取得
response = requests.get(url)

# responseからbsオブジェクトを生成
soup = BeautifulSoup(response.text, 'html.parser')

# idからデータを抽出
data = soup.find_all(id="plLog")

for data_text in data:
    data_text = data_text.text
    data_list = (data_text.split('\n'))

# 必要のない要素を削除
del data_list[0:51]

# headerを追加
header = ['節', '開催日', '相手', 'スコア', 'ホーム/アウェイ', '出場時間', 'ポジション', 'ゴール', 'アシスト', '攻撃CBP',
          'パスCBP', 'クロスCBP', 'ドリブルCBP', 'パスレシーブCBP', 'シュートCBP', 'ゴールCBP', '奪取P', '守備P', 'チーム']
data_list.insert(0, header)

# csvファイルopen
f = open("output.csv", "w", encoding='utf8')
writecsv = csv.writer(f, lineterminator='\n')

# 出力
writecsv.writerow(data_list)

# CSVファイルclose
f.close()
