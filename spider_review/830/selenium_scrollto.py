from time import sleep

from selenium import webdriver

# 1.创建浏览器对象
browser = webdriver.Chrome()

# 2.获取链接
browser.get('https://www.zhihu.com/explore')
sleep(3)
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')
