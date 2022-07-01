import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Users\davud\Desktop\SeleniumD\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://opensource-demo.orangehrmlive.com/')

link = driver.find_element(By.XPATH, "//a[normalize-space()='OrangeHRM, Inc']")

link.click()
# print(driver.current_window_handle)

# parent_window = driver.window_handles[0]
# child_window = driver.window_handles[1]
winids = driver.window_handles


# driver.switch_to.window(child_window)
# title_of_child_window = driver.title
# print(title_of_child_window)

# for wID in winids:
#      driver.switch_to.window(wID)
#      print(driver.title)



time.sleep(10)

for wId in winids:
    driver.switch_to.window(wId)
    if driver.title == 'OrangeHRM':# or and if driver.title == 'xyz'
        driver.close()


