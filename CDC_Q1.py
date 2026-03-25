from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://cathaybk.com.tw/cathaybk/")
# 簡單版
# container = driver.find_element(By.CSS_SELECTOR, "div.animate-fade-up")
#
# divs = container.find_elements(By.CSS_SELECTOR, "span.text-center")
#
# for div in divs:
#     print(div.text)
# ai優化版
wait = WebDriverWait(driver, 3)

container = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div.animate-fade-up"))
)

items = container.find_elements(By.CSS_SELECTOR, "a")

keywords = ["/personal/", "/eservice/"]

for item in items:
    href = item.get_attribute("href")

    if href and any(k in href for k in keywords):
        text = item.find_element(By.CSS_SELECTOR, "span:last-child").text
        print(text, href)

