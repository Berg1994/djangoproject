import urllib.request
import urllib.error

url = 'https://www.cuiqingcai.com/index.html'
request = urllib.request.Request(url)
try:
    response = urllib.request.urlopen(request)
except urllib.error.HTTPError as e:
    print('错误', e.reason, e.code, e.headers, sep='\n')
except urllib.error.URLError as e:
    print('错误', e)

else:
    print(response)


