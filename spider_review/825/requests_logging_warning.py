import requests
import logging

logging.captureWarnings(True)

res = requests.get('https://www.12306.cn',verify=False)

print(res)

