# author:  freelaeder
# ----
# date:  2022/4/15 11:18
from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
# 打印title
print(driver.title)
# 窗口全屏
driver.maximize_window()
# 关闭选项卡
# driver.close()

sleep(3)
# 关闭浏览器
driver.quit()
