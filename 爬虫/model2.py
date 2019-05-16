#!/anaconda3/bin/python
# @Time    : 2019-05-15 09:07
# @Author  : zhou
# @File    : model2
# @Software: PyCharm
# @Description: 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = 'https://mail.qq.com'
driver = webdriver.Chrome()
driver.get(url)

driver.implicitly_wait(5)  # 隐式等待
driver.maximize_window()  # 窗口最大化

# 填充用户名和密码
driver.find_element_by_id('qqLoginTab').click()
driver.switch_to.frame('login_frame')
driver.find_element_by_id('u').send_keys('1214794891')
elem = driver.find_element_by_id('p')

elem.send_keys('')
elem.send_keys(Keys.RETURN)  # 回车

# driver.find_element_by_xpath('//*[@id="gb_70"]').click()# 点击  # xpath   // 表示从任意节点开始选择

# 点击写信按钮
driver.find_element_by_xpath('//*[@id="composebtn"]').click()
# 定位到收件人框
driver.switch_to.frame('mainFrame')
driver.find_element_by_xpath('//*[@id="toAreaCtrl"]/div[2]/input').send_keys('401700108@qq.com')
# 定位到主题
driver.find_element_by_xpath('//*[@id="subject"]').send_keys('test')
# 定位到正文
iframe = driver.find_element_by_class_name('qmEditorIfrmEditArea')
driver.switch_to.frame(iframe)

driver.find_element_by_xpath('/html/body').send_keys('正文')

driver.switch_to.parent_frame()
driver.find_element_by_name('sendbtn').click()

time.sleep(5)
driver.quit()




