import requests

with open('./_request.py','rb') as f:
    r = requests.post('http://httpsbin.org/post',files=f)
    print(r.text)


