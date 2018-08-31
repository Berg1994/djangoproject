import urllib.request
import urllib.parse
import urllib.error

word = input('请输入搜索词')

url = 'https://www.baidu.com/s?'
headers = {
    'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

data = {
    'wd': word
}

#解析成百分号编码
query_string = urllib.parse.urlencode(data)
print(query_string)

#拼接链接
urls = url + query_string

# 创建请求对象
request = urllib.request.Request(url=urls, headers=headers)

response = urllib.request.urlopen(request)
# response = urllib.request.urlopen(urls)

print(response)
print(response)

# 写入文本
filename = word + '.html'



try:
    with open(filename, 'wb') as f:
        f.write(response.read())
except IOError as e:
    print(e)
