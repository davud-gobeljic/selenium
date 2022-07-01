from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from selenium.webdriver import Keys

#headless mode

def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    service_obj = Service(r"C:\Users\davud\Desktop\SeleniumD\chromedriver.exe")
    ops = webdriver.ChromeOptions()
    ops.headless = True
    driver = webdriver.Chrome(service=service_obj, options=ops)
    return driver

driver = headless_chrome()


driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://demo.nopcommerce.com/')

#capture cookie from browser
cookies = driver.get_cookies()
print(len(cookies))

#capture all the cookies
for c in cookies:
    print(c)

print('----------------------------------\n\n')

for c in cookies:
    print(c.get('name'), ":", c.get('value'))


# acc new cookie
driver.add_cookie({"name":"new_cookie","value":"123456"})
cookies_new = driver.get_cookies()
print("new size of the cookies", len(cookies_new))


# delete specific cookie

driver.delete_cookie('new_cookie')
driver.delete_all_cookies()