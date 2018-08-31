import requests

url = 'http://www.httpbin.org/post'
data = {
    'name': 'berg'
}

session = requests.Session()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'
}

request = requests.Request('POST',url,data=data,headers=headers)
prepard = session.prepare_request(request)

r = session.send(prepard)

print(r.text)