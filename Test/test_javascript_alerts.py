import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By



service_obj = Service(r"C:\Users\davud\Desktop\SeleniumD\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
js_prompt = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']")
js_prompt.click()
alert_window = driver.switch_to.alert
print(alert_window.text)
alert_window.send_keys("Sta ima")
alert_window.accept()