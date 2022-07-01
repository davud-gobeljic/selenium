import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By


service_obj = Service(r"C:\Users\davud\Desktop\SeleniumD\chromedriver.exe")
case = webdriver.Chrome(service=service_obj)

case.get("https://demo.nopcommerce.com/register")
#case.maximize_window()

searchbox = case.find_element(By.ID, "small-searchterms")
print("Searchbox is displayed = ",searchbox.is_displayed(),"\nSearchbox is enabled = ", searchbox.is_enabled(),"\nSearchbox is selected = ", searchbox.is_selected())

rd_male = case.find_element(By.ID, "gender-male")
rd_male.click()
rd_female = case.find_element(By.ID, "gender-female")
time.sleep(1)

print(rd_male.is_selected())
print(rd_female.is_selected())

if case.title == "Demo commerce":
    print("Title is correct")
else:
    print("wrong title")
