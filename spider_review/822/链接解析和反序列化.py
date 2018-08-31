import urllib.request
import urllib.parse

url = 'https://www.baidu.com?name=berg&age=18'
#解析链接 包含协议，域名，路径，参数，查询，锚点
url_ele = urllib.parse.urlparse(url)
# print(url_ele)
#反序列化 拼接链接
url_params = urllib.parse.parse_qs(url)
print(url_params)
url_tuple = urllib.parse.parse_qsl(url)
print(url_tuple)

data1 = {'kw':'非洲大萨满'}
data2 = 'kw=非洲大萨满'

print(urllib.parse.quote(data2))
print(urllib.parse.urlencode(data1))

