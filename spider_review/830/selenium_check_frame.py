import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchAttributeException

browser = webdriver.Chrome()

url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'

browser.get(url)
#切换
browser.switch_to.frame('iframeResult')

try:
    logo = browser.find_element_by_class_name('logo')
except NoSuchAttributeException:
    print('NO LOGO')
#切到父级
browser.switch_to.parent_frame()
logo = browser.find_element_by_class_name('logo')
print(logo)
print(logo.text)
