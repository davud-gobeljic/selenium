import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
import requests as requests

service_obj = Service(r"C:\Users\davud\Desktop\SeleniumD\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()



# links = driver.find_elements(By.TAG_NAME, 'a')
# print(len(links))
#
# for link in links:
#     print(link.text)



# HOW TO HANDLE BROKEN LINKS ---------- WE NEED TO INSTALL PACKAGE THROUGH FILE-SETTINGS-PROJECT INTEPRETETER- + - requests

linkovi = driver.find_elements(By.TAG_NAME, 'a')
count = 0

for link in linkovi:
    url = link.get_attribute('href')
    try:
        res = requests.head(url)
    except:
        None
    if res.status_code >= 400:
        print(url, "This is the broken link")
        count = count + 1
    else:
        print("Valid link")

print("Total number of broken links is: ", count)










