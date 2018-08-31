from selenium import webdriver

#1.创建浏览器对象
browser = webdriver.Chrome()

#2.获取链接
browser.get('https://www.taobao.com')

lis = browser.find_element_by_css_selector('.service-bd li')
print(lis)
browser.close()
