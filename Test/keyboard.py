from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains as AC
from selenium.webdriver import Keys

service_obj = Service(r"C:\Users\davud\Desktop\SeleniumD\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://text-compare.com/")

tab1 = driver.find_element(By.ID, "inputText1")
tab2 = driver.find_element(By.ID, "inputText2")

tab1.send_keys("Welcome to the Selenium")

action = AC(driver)
# # ctrl + a

# action.key_down(Keys.CONTROL)
# action.send_keys('a')
# action.key_up(Keys.CONTROL)
# action.perform()
time.sleep(1)

action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()

time.sleep(0.5)
# ctrl + c
action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

# tab
time.sleep(0.5)
action.send_keys(Keys.TAB).perform()

# ctrl + v
time.sleep(0.5)
action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()