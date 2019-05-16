#!/anaconda3/bin/python
# @Time    : 2019-05-15 08:25
# @Author  : zhou
# @File    : model
# @Software: PyCharm
# @Description: 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

secs = 10
# url = 'https://www.baidu.com'
url = 'http://10.132.246.246'
driver = webdriver.Chrome()
driver.get(url)

driver.implicitly_wait(5)  # 隐式等待
driver.maximize_window()  # 窗口最大化

# 填充用户名和密码
driver.find_element_by_name('username').send_keys('16211160127')
elem = driver.find_element_by_name('password')
elem.send_keys('password')
# elem.send_keys(Keys.RETURN)  # 回车

driver.find_element_by_xpath('//*[@id="gb_70"]').click()# 点击  # xpath   // 表示从任意节点开始选择





