import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Users\davud\Desktop\SeleniumD\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

driver.switch_to.frame("packageListFrame")
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
driver.switch_to.default_content()

driver.switch_to.frame('packageFrame')
driver.find_element(By.LINK_TEXT, "WebDriver").click()
driver.switch_to.default_content()


driver.switch_to.frame('classFrame')
driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/div[1]/ul/li[8]").click()
driver.switch_to.default_content()