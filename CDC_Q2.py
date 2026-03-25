from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://cathaybk.com.tw/cathaybk/")
topmenu = driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[1]")
topmenu.click()
time.sleep(3)
subm = driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[3]/div[2]/a[5]")
subm.click()
time.sleep(3)
calcm = driver.find_element(By.XPATH,"/html/body/form/div[4]/main/div/section[1]/div/div/a[1]/div/div[2]")
calcm.click()
time.sleep(3)
money = driver.find_element(By.XPATH,'//input[@name="Amount"]')
money.send_keys("1000")
time.sleep(3)
fee = driver.find_element(By.XPATH,'//input[@name="Fee"]')
fee.send_keys("5000")
time.sleep(3)
periodrate = driver.find_element(By.XPATH,'//input[@name="periodrate1"]')
periodrate.send_keys("1.38")
time.sleep(3)
submitbtn = driver.find_element(By.XPATH,'//*[@id="formSubmitBtn"]')
submitbtn.click()
time.sleep(3)

#檢查畫面與預期數字是否相同
rm = driver.find_element(By.XPATH,'//*[@id="mainform"]/div[4]/main/div/div[3]/div/section/div/div/div[1]/div[1]/div[1]/span')
# print (rm.text)
assert rm.text =='1,100萬元', "貸款金額錯誤"

rp = driver.find_element(By.XPATH,'//*[@id="mainform"]/div[4]/main/div/div[3]/div/section/div/div/div[1]/div[1]/div[2]/span')
# print (rp.text)
assert rp.text =='1.41%', "百分比錯誤"

fm = driver.find_element(By.XPATH,'//*[@id="mainform"]/div[4]/main/div/div[3]/div/section/div/div/div[1]/div[2]/div/div/div[1]/div[2]/span')
# print (fm.text)
assert fm.text =='283,727', "1-35月還款金額錯誤"

lm = driver.find_element(By.XPATH,'//*[@id="mainform"]/div[4]/main/div/div[3]/div/section/div/div/div[1]/div[2]/div/div/div[2]/div[2]/span')
# print (lm.text)
assert lm.text =='283,732', "36月還款金額錯誤"

time.sleep(3)
driver.quit()
# div = driver.find_element(By.CLASS_NAME,"cubre-o-menu__btn")
# div.click()
#
# time.sleep(20)

##拿第一個
# divs = deiver.find_element(By.CLASS_NAME, "cubre-m-quickLink__text")
# print(divs.text)

# ##拿全部
# divs = deiver.find_elements(By.CLASS_NAME, "cubre-m-quickLink__text")
# for div in divs:
#     print(div.text)
