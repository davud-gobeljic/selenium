from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Users\davud\Desktop\SeleniumD\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get('https://testautomationpractice.blogspot.com/')

# count number of rows and columns

number_of_rows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr"))
# or  "//table[@name='BookTable']//tr"

number_of_columns = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr/th"))

print("Number of rows is: ", number_of_rows)
print("Number of columns is: ", number_of_columns)


# Read specific row and column data

zzz = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[2]").text
print(zzz)



# Read all the columns and all data

print("printing all the rows and column data............")

for r in range(2, number_of_rows + 1):
    for c in range(1, number_of_columns + 1):
        data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(data, end='      ')
    print()


print("-------------------------------\n---------------------------------")
# Read data based on conditions


for r in range(2, number_of_rows + 1):
    authorName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if authorName == "Amit" or authorName == "Mukesh":
        bookName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[1]").text
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]").text
        print(bookName,"  ", authorName, "  ", price)

