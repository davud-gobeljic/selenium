from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains as AC


service_obj = Service(r"C:\Users\davud\Desktop\SeleniumD\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
min_price = driver.find_element(By.XPATH, "//span[1]") # {'x': 59, 'y': 250}
max_price = driver.find_element(By.XPATH, "//span[2]") # {'x': 1022, 'y': 250}


time.sleep(2)
print(min_price.location)
print(max_price.location)

act = AC(driver)

act.drag_and_drop_by_offset(min_price, 100, 0).perform()
time.sleep(1)
act.drag_and_drop_by_offset(max_price, -100, 0).perform()

print("------------------NEW XY -----------------------")
print(min_price.location)
print(max_price.location)


