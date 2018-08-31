from selenium import webdriver

# 1.创建浏览器对象
browser = webdriver.Chrome()

# 2.获取页面链接
browser.get('https://www.taobao.com')

# .获取输入框
input_first = browser.find_element_by_id('q')
input_second = browser.find_element_by_css_selector('#q')
input_third = browser.find_element_by_xpath('//*[@id="q"]')
print(input_first, input_second, input_third)
browser.close()


