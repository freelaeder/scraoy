# author:  freelaeder
# ----
# date:  2022/4/18 20:47

import time
from time import sleep

from selenium import webdriver

# 创建驱动的时候 把options添加上
from selenium.webdriver.common.by import By

# - 1 打开https://i.qq.com/
# - 2 找到帐号密码登录的按钮  点击一下
# - 3 找到帐号输入框 输入
# - 4 找到密码输入框 输入密码
# - 5 找到登录按钮 点一下

driver = webdriver.Chrome()
# 1 打开https://i.qq.com/
driver.get("https://i.qq.com/")

# 发现 帐号密码登录按钮 在iframe内部  需要先定位iframe标签  跳转到iframe内部 再去获取
login_frame = driver.find_element_by_id("login_frame")
driver.switch_to.frame(login_frame)

# - 2 找到帐号密码登录的按钮  点击一下
switcher_plogin = driver.find_element_by_id("switcher_plogin")
# switcher_plogin = driver.find_element(By.XPATH, '//*[@id="switcher_plogin"]')
switcher_plogin.click()
# - 3 找到帐号输入框 输入
u = driver.find_element_by_id("u")
time.sleep(1)
u.send_keys("2590131280")
p = driver.find_element_by_id("p")
time.sleep(1)
p.send_keys('q1w2e3!(()')
time.sleep(1)
# - 5 找到登录按钮 点一下
login_button = driver.find_element_by_id("login_button")
login_button.click()

sleep(5)
driver.quit()  # 关闭浏览器
