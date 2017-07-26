import requests

r = requests.get('http://weather.livedoor.com/forecast/webservice/json/v1?city=130010')
print(r.status_code) # 200(正常終了を表すステータスコード)が表示される
print(r.text[:100]) # レスポンスの先頭100文字
