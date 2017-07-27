import requests

r = requests.get('http://book.impress.co.jp/')
print(r.status_code)
