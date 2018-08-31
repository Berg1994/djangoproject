import urllib.request
import urllib.parse

url = 'http://fanyi.baidu.com/sug'

formdata = {
    'kw': 'berg'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.3',
}

data = urllib.parse.urlencode(formdata).encode('utf')
print(data)
# request = urllib.request.Request(url=url, headers=headers)
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf8'))
