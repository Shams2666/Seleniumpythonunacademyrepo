import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://unacademy.com/goal/upsc-civil-services-examination-ias-preparation/KSCGY")
driver.maximize_window()
driver.find_element(By.XPATH,"//span[normalize-space()='Log in']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@placeholder='Enter your mobile number']").send_keys("9972714110")
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
time.sleep(25)
driver.find_element(By.XPATH,"//button[normalize-space()='Verify OTP']").click()
time.sleep(10)
driver.find_element(By.XPATH,"//img[@alt='shams ']").click()
driver.find_element(By.XPATH,"//p[normalize-space()='Settings']").click()
time.sleep(10)
driver.find_element(By.XPATH,"//p[normalize-space()='Prior Plus Courses']").click()
time.sleep(5)
