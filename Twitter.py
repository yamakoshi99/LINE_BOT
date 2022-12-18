import tweepy
from pprint import pprint
import schedule
from time import sleep

# API情報を記入
BEARER_TOKEN        = "BEARER TOKEN"
API_KEY             = "API キー"
API_SECRET          = "API シークレット"
ACCESS_TOKEN        = "アクセストークン"
ACCESS_TOKEN_SECRET = "アクセストークンシークレット"


# クライアント関数を作成
def ClientInfo():
    client = tweepy.Client(bearer_token    = BEARER_TOKEN,
                           consumer_key    = API_KEY,
                           consumer_secret = API_SECRET,
                           access_token    = ACCESS_TOKEN,
                           access_token_secret = ACCESS_TOKEN_SECRET,
                          )

    return client

# ★メッセージを指定
message = "Hello World"

# 関数
def CreateTweet(message):
    tweet = ClientInfo().create_tweet(text=message)
    return tweet

# 関数実行・結果出力
pprint(CreateTweet(message))

# # メッセージを指定
# message = "Hello World"

# #01 定期実行するツイート関数を準備
# def CreateTweet(message):
#     tweet = ClientInfo().create_tweet(text=message)
#     return tweet

# #02 スケジュール登録(2日おきにツイート)
# schedule.every(2).days.do(CreateTweet,message=message)

# #03 イベント実行
# while True:
#     schedule.run_pending()
#     sleep(1)