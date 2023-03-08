import time
from webbrowser import get

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://unacademy.com/goal/upsc-civil-services-examination-ias-preparation/KSCGY")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@placeholder='Search courses, test series and educators']").send_keys("Water")
#driver.find_element(By.XPATH,"//div[@class='css-1i7s5mp']").
time.sleep(5)
driver.find_element(By.XPATH,"//a[@href='/search/water?source=Free+Home+Page']//div[@class='css-zhxa7k-Item e1p4w5690']").click()
time.sleep(10)