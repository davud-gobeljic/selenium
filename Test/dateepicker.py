from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_obj = Service(r"C:\Users\davud\Desktop\SeleniumD\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://jqueryui.com/datepicker/')
driver.switch_to.frame(0)
time.sleep(2)
driver.find_element(By.ID, "datepicker").click()

year = '2023'
month = 'August'
day = '24'
time.sleep(2)

while True:
    mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text


    if mon == month and yr == year:
        break
    else:
        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div/a[2]/span').click()
        #driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div/a[1]/span').click()



dat =driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for el in dat:
    if el.text == day:
        el.click()
        break
