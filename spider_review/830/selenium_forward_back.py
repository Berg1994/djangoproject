from selenium import webdriver
import time

#1.创建浏览器对象
browser = webdriver.Chrome()

#2.打开链接
browser.get('https://www.baidu.com')
browser.get('https://www.taobao.com')
browser.get('https://www.baidu.com')
browser.back()
time.sleep(2)
browser.forward()
browser.close()
