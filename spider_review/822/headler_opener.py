import urllib.request

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.3',
}

url = 'http://www.baidu.com/s?ie=UTF-8&wd=ip'

handler = urllib.request.ProxyHandler(proxies={'http': '111.155.116.216:8123'})

opener = urllib.request.build_opener(handler)

urllib.request.install_opener(opener)

req = urllib.request.Request(url, headers=headers)

resp = urllib.request.urlopen(req, timeout=5)

print(type(resp.code))
print(resp.read().decode('utf8'))
# if resp == 200:

# with open('代理.html', 'wb') as fp:
# 	fp.write(r.read())
