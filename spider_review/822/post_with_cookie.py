import urllib.request
import urllib.parse
import requests
url = 'http://fanyi.baidu.com/v2transapi'

res = requests.get(url)

print(res.status_code)