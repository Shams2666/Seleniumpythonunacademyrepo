import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://unacademy.com/")
driver.maximize_window()
time.sleep(10)
driver.find_element(By.XPATH,"//a[text()='About Us']").click()
time.sleep(10)
