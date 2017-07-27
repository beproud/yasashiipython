import requests

r = requests.get('http://weather.livedoor.com/forecast/webservice/json/v1?city=130010')
print(r.status_code)
print(r.text[:100])
