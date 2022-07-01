from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains as AC

service_obj = Service(r"C:\Users\davud\Desktop\SeleniumD\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element(By.ID, "txtUsername").send_keys('Admin')
driver.find_element(By.ID, "txtPassword").send_keys('admin123')
driver.find_element(By.ID, "btnLogin").click()
time.sleep(2)

admin = driver.find_element(By.XPATH, "//*[@id='menu_admin_viewAdminModule']/b")
usermgm = driver.find_element(By.XPATH, "//*[@id='menu_admin_UserManagement']")
users = driver.find_element(By.XPATH, "//*[@id='menu_admin_viewSystemUsers']")

#mouse hover

act = AC(driver)
act.move_to_element(admin).move_to_element(usermgm).move_to_element(users).click().perform()
driver.quit()
# act.context_click() desni klik
# act.double_click()
# act.drag_and_drop()
# example = if we want to know locaiton of certain web element minLoad = driver.find.elem...
# print(minLoad.location)

