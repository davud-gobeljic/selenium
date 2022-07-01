from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

# ctrl+b pychram or f12 vscode

service_obj = Service(r"C:\Users\davud\Desktop\SeleniumD\chromedriver.exe")
case = webdriver.Chrome(service = service_obj)

case.get("https://www.olx.ba")
case.maximize_window()



time.sleep(2)

try:
    cookie = case.find_element(By.XPATH, '//*[@id="cookiesBar"]/p/button')
    cookie.click()
except:
    print("No cookie this time")




case.find_element(By.ID, "loginbtn").click()

case.find_element(By.ID, "username").send_keys("satici")
time.sleep(1)

case.find_element(By.ID, "password").send_keys("pikpikpik")
time.sleep(1)

case.find_element(By.ID, "btnlogin1").click()
time.sleep(1)

case.find_element(By.ID, "searchinput").send_keys("juka01")
time.sleep(3)

case.find_element(By.XPATH, '//*[@id="sugcontent"]/ul/li[1]/a').click()
time.sleep(1)

case.find_element(By.XPATH, '//*[@id="art_45108736"]/div[1]/a').click()
time.sleep(1)

case.find_element(By.ID, "posaljiporuku").click()
time.sleep(2)

case.find_element(By.ID, "tekst_poruke").send_keys("koja je najniza za kes")
