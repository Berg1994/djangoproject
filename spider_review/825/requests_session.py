import requests

se = requests.Session()

url = 'http://httpbin.org/cookies/set/hello/12345'
se.get(url)
r = se.get('http://httpbin.org/cookies')
print(r.text)
