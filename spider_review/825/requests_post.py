import requests

data = {
    'name':'berg',
    'age':22
}

r = requests.post('https://www.httpbin.org/post',data=data)

print(r.text)
#text 是文档 是字符串类型    content是二进制数据
print(r.content)
