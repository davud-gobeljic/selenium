import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By


service_obj = Service(r"C:\Users\davud\Desktop\SeleniumD\chromedriver.exe")
case = webdriver.Chrome(service=service_obj)

case.get("https://www.snapdeal.com")
time.sleep(2)
case.get("https://www.amazon.com")
time.sleep(2)
case.back()
time.sleep(1)
case.forward()
time.sleep(2)
case.refresh()

menu_item = case.find_element(By.XPATH, '//*[@id="nav-xshop"]/a[1]')
print(menu_item.text)


try:
    gift_cars = case.find_element(By.LINK_TEXT, "Gift cards")
    gift_cars.click()
except:
    print("Not the right text")