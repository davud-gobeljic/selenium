from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains as AC
from selenium.webdriver import Keys
import os

location = os.getcwd()

service_obj = Service(r"C:\Users\davud\Desktop\SeleniumD\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/")
action = AC(driver)
time.sleep(2)

# driver.save_screenshot("C:\\Users\\davud\\PycharmProjects\\QA\\Test\\homepage.png")
# driver.save_screenshot(location + "homapag353e.png")
driver.save_screenshot(os.getcwd() + "\\hmp.png")
driver.get_screenshot_as_png()




