import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import sched, time, datetime
def line_notify_with_image(message,filename):
    line_notify_token = 'SvGq9MeunxYswjve6bI5FyCJPZEVhItfBYP6xy4abnG'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}
    files = {'imageFile': open(filename, 'rb')}
    requests.post(line_notify_api, data=payload, headers=headers, files=files)

def check_today_weather():
    filename = "本日の天気.png"

    # クローラーの起動
    driver = webdriver.Firefox()

    #指定したドライバの要素が見つかるまでの待ち時間を10秒に設定
    driver.implicitly_wait(10)

    # Yahooの天気サイトにアクセス(かながわ)
    driver.get('https://weather.yahoo.co.jp/weather/jp/14/?day=1')

    # ソースコードを取得
    html = driver.page_source

    driver.get('https://weather.yahoo.co.jp/weather/jp/14/4610.html')
    #申込結果の画面をキャプチャする
    driver.save_screenshot(filename)
    # ブラウザを終了する
    driver.quit()

    # HTMLをパースする
    soup = BeautifulSoup(html, 'lxml') # または、'html.parser'

    # スクレイピングした《今日の日本の天気予報の概況》を変数に格納
    message = soup.select_one('#condition > p.text').get_text()

    # LINEに通知させる
    line_notify_image(message,filename)

import requests
from bs4 import BeautifulSoup
from pytrends.request import TrendReq

#LINE Notifyと連携するためのtoken
line_notify_token = 'SvGq9MeunxYswjve6bI5FyCJPZEVhItfBYP6xy4abnG'
line_notify_api = 'https://notify-api.line.me/api/notify'

#requests.getでHTMLを取得
r = requests.get('https://weather.yahoo.co.jp/weather/jp/13/4410.html')
#BeautifulSoupを使用してパース
soup = BeautifulSoup(r.content, "html.parser")

wc = soup.find(class_="forecastCity")
#print(wc)

#.strip():前後の空白文字の削除・.splitlines():改行コードで分割
ws = [i.strip() for i in wc.text.splitlines()]
#print(ws)

#リスト内包表記で""でないものをリスト化
wl = [i for i in ws if i != ""]
#print(wl)

#message = ("\n" + "東京都:" + wl[0] + "\n" + wl[1] + "\n"  + "最高気温:" + wl[2] + "\n"+ "最低気温:" + wl[3] + "\n" + "\n" + wl[18] + "\n" + wl[19] + "\n" + "最高気温:" + wl[20] + "\n" + "最低気温:" + wl[21] )


pytrends = TrendReq(hl='ja-JP', tz=-540)
py = pytrends.trending_searches(pn='japan')


#LINENotifyへ通知の記述
payload = {'message': py}
headers = {'Authorization': 'Bearer ' + line_notify_token}
line_notify = requests.post(line_notify_api, data=payload, headers=headers)
