# author:  freelaeder
# ----
# date:  2022/4/15 15:50
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.baidu.com/s?ie=UTF-8&wd=python")

logo = driver.find_element(By.ID, 'result_logo')
