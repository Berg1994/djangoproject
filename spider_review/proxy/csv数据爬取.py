import requests
url = 'https://api.github.com/repos/pandas-dev/pandas/issues'


resp = requests.get(url)
# print(resp)
data = resp.json()

print(data[0]['title'])

#jira 禅道