from selenium import webdriver
from selenium.webdriver import ActionChains

# 1.创建浏览器对象
browser = webdriver.Chrome()

# 2.获取链接
browser.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

browser.switch_to.frame('iframeResult')

source = browser.find_element_by_css_selector('#draggable')

target = browser.find_element_by_css_selector('#droppable')
#创建动作链实例
actions = ActionChains(browser)
#拖动方法
actions.drag_and_drop(source,target)
#执行操作
actions.perform()
