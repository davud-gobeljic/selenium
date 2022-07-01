from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys

service_obj = Service(r"C:\Users\davud\Desktop\SeleniumD\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://demo.nopcommerce.com/')

press = Keys.CONTROL, Keys.RETURN
driver.find_element(By.XPATH, "//a[@class='ico-login']").send_keys(press)
driver.switch_to.window(0)
driver.switch_to.new_window('tab')
driver.switch_to.new_window('window ')