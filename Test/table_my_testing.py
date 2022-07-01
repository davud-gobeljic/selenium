from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Users\davud\Desktop\SeleniumD\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://testautomationpractice.blogspot.com/')

num_of_row = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))
num_of_col = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//th"))

print('No of row: ', num_of_row, '\nNo of col : ', num_of_col)

sel = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[2]/td[3]").text
print(sel)


for r in range(2, num_of_row + 1):
    for c in range(1, num_of_col + 1):
        data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(data , end="  ")
    print()





driver.close()
