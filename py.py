from pytrends.request import TrendReq
pytrends = TrendReq(hl='ja-JP', tz=-540)

kw_list = ['ソフトバンク']

pytrends.build_payload(kw_list=kw_list,
    timeframe='2019-01-01 2021-06-30',
    geo='JP')

pytrends.interest_over_time()
