from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains as AC


service_obj = Service(r"C:\Users\davud\Desktop\SeleniumD\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
# driver.execute_script("window.scrollBy(0, 3000)","")
val = driver.execute_script("return window.pageYOffset;")
print(val)

flag = driver.find_element(By.XPATH, "//img[@alt='Flag of United States of America']")
driver.execute_script("arguments[0].scrollIntoView();", flag)
value = driver.execute_script("return window.pageYOffset;")
print(value)

# driver.execute_script("window.scrollBy(0, document.body.scrollHeight)") do kraja
time.sleep(2)
driver.execute_script("window.scrollBy(0, -document.body.scrollHeight)")