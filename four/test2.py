# author:  freelaeder
# ----
# date:  2022/4/18 14:35

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
# 打印title
print(driver.title)
# 窗口全屏
driver.maximize_window()
# 关闭选项卡
# driver.close()
# 当前url
print(driver.current_url)
# 当前所有cookie
print(driver.get_cookies())
# 获取源码
# print(driver.page_source)
# sleep(3)
# 关闭浏览器
# driver.quit()
