import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException


service_obj = Service(r"C:\Users\davud\Desktop\SeleniumD\chromedriver.exe")
case = webdriver.Chrome(service=service_obj)
case.implicitly_wait(10)
case.get("https://itera-qa.azurewebsites.net/home/automation")
case.maximize_window()

mon_to_sun = case.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")

print(len(mon_to_sun))

# # first option
# for i in range(len(mon_to_sun)):
#     mon_to_sun[i].click()

# second option
# for day in mon_to_sun:
#     day.click()


# select by choice

# for day in mon_to_sun:
#     weekname = day.get_attribute('id')
#     if weekname == 'monday' or weekname == 'friday' or weekname == 'sunday':
#         day.click()



#select last 2 checkboxes

for i in range(len(mon_to_sun)-2, len(mon_to_sun)):
    mon_to_sun[i].click()

time.sleep(2)

#select first two checkboxes

for i in range(len(mon_to_sun)):
    if i < 2:
        mon_to_sun[i].click()

time.sleep(2)

for check in mon_to_sun:
    if check.is_selected():
        check.click()




















