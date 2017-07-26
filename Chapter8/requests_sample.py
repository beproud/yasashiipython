import requests

r = requests.get('http://book.impress.co.jp/category/series/easybook/')
print(r.status_code) # 200（正常終了を表すステータスコード）が表示される
print(r.text[:130]) # HTMLの先頭
