from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_obj = Service(r"C:\Users\davud\Desktop\SeleniumD\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/index.php/dashboard")

username = driver.find_element(By.ID, 'txtUsername').send_keys('Admin')
password = driver.find_element(By.ID, 'txtPassword').send_keys('admin123')

button  = driver.find_element(By.ID, 'btnLogin').click()
time.sleep(3)

driver.find_element(By.XPATH, "//b[normalize-space()='Admin']").click()
driver.find_element(By.XPATH, "//a[@id='menu_admin_UserManagement']").click()
driver.find_element(By.XPATH, "//a[@id='menu_admin_viewSystemUsers']").click()

table_rows = len(driver.find_elements(By.XPATH, "//table[@id='resultTable']/tbody/tr"))
print("table row", table_rows)


enabled = 0

for r in range(1 , table_rows + 1):
    data = driver.find_element(By.XPATH, "//table[@id='resultTable']/tbody/tr["+str(r)+"]/td[5]").text
    admin = driver.find_element(By.XPATH, "//table[@id='resultTable']/tbody/tr["+str(r)+"]/td[2]").text
    if data == "Enabled":
        enabled = enabled + 1

print("Enabled accounts : ", enabled)
print("Disabled accounts : ", table_rows - enabled)

driver.close()