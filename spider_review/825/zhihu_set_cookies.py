import requests

cookies = '_zap=1ad46601-9b12-41bf-9037-f19f02aa423b; d_c0="ADDmos64_w2PTquoeeGA8fHj8niuJNHjat8=|1533279505"; q_c1=fb705199a9be46108cae93a279530329|1533279507000|1533279507000; _xsrf=GP9N4XKwVS694HX6YTPdlDPhEj02Q4NK; __utma=51854390.681961762.1534324779.1534324779.1534324779.1; __utmz=51854390.1534324779.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.000--|3=entry_date=20180803=1; l_cap_id="YzBiZDgwYmUxMWMwNDFhNmI0NWJkMjAxOGRmOWMzYWY=|1535210830|5a07877e606a72448f9799e697efc0dfb684afb7"; r_cap_id="MmFjNjJhMzE4ZTgyNDM1YWJkZDg2NTZkZmEyZDcwNDE=|1535210830|a66e7ed6c9080d708f2a2dbdc31799ebc7c6daa9"; cap_id="NWQxODhkNDkzYzFhNDVkOTllNmZkNTQ1N2I2MjE5YWI=|1535210830|736b42e2cafc52382e014ee24db13bc8dcfb1eaa"; tgw_l7_route=860ecf76daf7b83f5a2f2dc22dccf049; capsion_ticket="2|1:0|10:1535274364|14:capsion_ticket|44:MmVmZDIyZWQ3ZDk3NDZjY2JiMGViNTk3MWZkZTMyZmQ=|656f22f8e459c8eaeb54caa4c8dcfe4234c497db719370f1b05b2092801f9c4d"; z_c0="2|1:0|10:1535274369|4:z_c0|92:Mi4xMlZyWEFnQUFBQUFBTU9haXpyal9EU1lBQUFCZ0FsVk5nYnR2WEFDSFZwUmZVcHhoN3VoZkFVN3hmOXJIb0tsd1R3|b835e67b137f90c02f033e7538d82003f25fc6f96ffc6bbca2e2fc55bcb16337"'

jar = requests.cookies.RequestsCookieJar()
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}


url = 'https://www.zhihu.com'

for cookie in cookies.split(';'):
    print(cookie)
    # print('*' * 100)
    key,value = cookie.split('=',1)
    print(key,value)
    jar.set(key,value)
r = requests.get(url=url,headers=headers,cookies=jar)
print(r)