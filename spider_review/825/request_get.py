import requests 

data = {
    'name':'berg',
    'age':22
}

r = requests.get('https://www.httpbin.org/get',params=data)

print(r)