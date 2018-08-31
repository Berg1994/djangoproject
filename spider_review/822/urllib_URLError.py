from urllib.error import URLError
import urllib.request 

url = 'https://www.cuiqingcai.com/index.html'
try:
    response = urllib.request.urlopen(url)
except URLError as e:
    print('错误', e)

