import requests

res = requests.get('https://www.12306.cn',verify=False)

print(res.status_code)
