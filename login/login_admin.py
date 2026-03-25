from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def adminlogin():
    driver = webdriver.Chrome()
    driver.get("https://test-report.zestplay.co/login")
    time.sleep(5)
    inputaccount = driver.find_element(By.XPATH,'//*[@id="account"]')
    inputaccount.send_keys("admin")
    time.sleep(3)
    inputpwd = driver.find_element(By.XPATH,'//*[@id="password"]')
    inputpwd.send_keys("aaaa1234")
    time.sleep(3)
    submitbtn = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div/form/div/div[4]/button')
    submitbtn.click()
    time.sleep(8)

