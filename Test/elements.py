import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By


service_obj = Service(r"C:\Users\davud\Desktop\SeleniumD\chromedriver.exe")
case = webdriver.Chrome(service=service_obj)
case.get("https://demo.nopcommerce.com/")

elementsss = case.find_elements(By.XPATH, "//div[@class='footer-upper']//a")

for element in elementsss:
    print(element.text)

