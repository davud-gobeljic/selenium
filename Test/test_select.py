import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
import requests as requests
from selenium.webdriver.support.select import Select as SE

service_obj = Service(r"C:\Users\davud\Desktop\SeleniumD\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://www.opencart.com/index.php?route=account/register")
# select = driver.find_element(By.XPATH, "//select[@id='input-country']") moze i ovako ali se onda select varijabla ukljuci u SE
select_country_obj_inst = SE(driver.find_element(By.XPATH, "//select[@id='input-country']")) #instanca predefinasne klase Select as SE
time.sleep(2)
# select_country_obj_inst.select_by_visible_text("Bosnia and Herzegowina")
select_country_obj_inst.select_by_value("10")
# select_country_obj_inst.select_by_index("2")

all_options = select_country_obj_inst.options

for option in all_options:
    print(option.text)


for opt in all_options:
    if opt.text == "Bosnia and Herzegowina":
        opt.click()
        break


print("-------------------------------------------------------")

all_possibile_options = driver.find_elements(By.XPATH, '//*[@id="input-country"]/option')
print(len(all_possibile_options))

for one_opt in all_possibile_options:
    print(one_opt.text)


zzaa = driver.find_elements(By.TAG_NAME, 'a')
print('----------------------------')
print(len(zzaa))
print('----------------')

for z in zzaa:
    print(z.text)