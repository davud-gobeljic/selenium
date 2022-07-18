import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture()

def setup():
    service_obj = Service(r"C:\Users\davud\Desktop\SeleniumD\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver



# def setup():
#     driver =  webdriver.Chrome()
#     return driver
#