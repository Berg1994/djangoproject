import urllib.request

response = urllib.request.urlopen('https://www.python.org')
#获取响应对象
print(type(response))
#链接
print(response.url)
#返回信息
print(response.msg)
#状态码
print(response.status)
#版本
print(response.version)
#响应头
# print(response.getheaders())
#服务器信息
print(response.getheader('Server'))
# print(response.read().decode('utf8'))

