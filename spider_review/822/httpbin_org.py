import urllib.request
import urllib.parse

# 获取二进制的请求内容
data = urllib.parse.urlencode({'hello': 'word'}).encode('utf8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)

print(response.read().decode('utf8'))
