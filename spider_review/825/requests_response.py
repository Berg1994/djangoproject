import requests

r = requests.get('http://www.jianshu.com')
print(r.status_code)
print(r.headers)
print(r.history)
print(r.cookies)
print(r.url)
