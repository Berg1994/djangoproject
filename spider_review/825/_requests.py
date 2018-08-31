


import requests  


r = requests.get('https://www.python.org')  

print(r.status_code)
print(r.text)
print(r.contnet)
print(r.cookies)

