from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1.创建浏览器实例
browser = webdriver.Chrome()

# 2.获取链接
browser.get('https://www.taobao.com/')
# 创建显式等待实例
wait = WebDriverWait(browser, 10)
input = wait.until(EC.presence_of_all_elements_located((By.ID, 'q')))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
print(input, button)
