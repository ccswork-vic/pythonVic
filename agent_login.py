from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://test-report.zestplay.co/login")
time.sleep(5)
account =driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div/form/div/div[1]/div/div/div[1]/label')
print (account.text)
pwd =driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div/form/div/div[2]/div/div/div[1]')
print (pwd.text)
inputaccount = driver.find_element(By.XPATH,'//*[@id="account"]')
inputaccount.send_keys("admin")
time.sleep(3)
inputpwd = driver.find_element(By.XPATH,'//*[@id="password"]')
inputpwd.send_keys("aaaa1234")
time.sleep(3)
submitbtn = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div/form/div/div[4]/button')
submitbtn.click()
time.sleep(8)
successlogin = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/header/div[2]/div[1]/button/span[2]')
print ("你登入的帳號為：" + successlogin.text)
