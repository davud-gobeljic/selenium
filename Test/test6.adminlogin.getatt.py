import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By


service_obj = Service(r"C:\Users\davud\Desktop\SeleniumD\chromedriver.exe")
case = webdriver.Chrome(service=service_obj)
case.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
time.sleep(1)
input_usr = case.find_element(By.XPATH, '//*[@id="Email"]')
input_usr.clear()
time.sleep(1)


input_usr.send_keys("davud@live.com")
time.sleep(2)
print(input_usr.text)
print(input_usr.get_attribute('value'))
