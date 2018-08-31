import requests
from requests.packages import urllib3#

#通过调用模块的函数不显示警告
urllib3.disable_warnings()

res = requests.get('https://www.12306.cn',verify=False)
print(res.status_code)




