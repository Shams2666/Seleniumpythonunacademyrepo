import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://unacademy.com/goal/upsc-civil-services-examination-ias-preparation/KSCGY")
driver.maximize_window()
driver.find_element(By.XPATH,"//div[@class='css-1i7s5mp']").click()
time.sleep(10)
