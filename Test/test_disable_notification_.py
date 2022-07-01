from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time

# webdriver chromeotions is to enable chrome options, then we can adjust browser option like pop notifications through add.argument
ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

service_obj = Service(r"C:\Users\davud\Desktop\SeleniumD\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=ops)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://whatmylocation.com/show-current-address.htm")
