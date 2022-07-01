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
case.get("https://www.google.com")
case.maximize_window()
search_bmw = case.find_element(By.CLASS_NAME, "s75CSd")
search_bmw.send_keys("BMW R1200GS Adventure")
search_bmw.send_keys(Keys.ENTER)


my_wait_obj = WebDriverWait(case, 10,poll_frequency=2 ,ignored_exceptions=[NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException, Exception]) #explicit wait declaration
search_link = my_wait_obj.until(EC.presence_of_element_located((By.XPATH, "//*[@id='rso'']/div[3]/div/div/div[1]/div/div[1]/a")))
search_link.click()


