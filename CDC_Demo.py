
from selenium import webdriver
from selenium.webdriver.common.by import By

# PATH = "/Users/user/Downloads/chromedriver_mac64/chromedriver"
deiver = webdriver.Chrome()
deiver.get("https://cathaybk.com.tw/cathaybk/")
# print(deiver.title)
divs = deiver.find_elements(By.CLASS_NAME, "cubre-m-quickLink__text")
for div in divs:
    print(div.text)
#print(div.text)
