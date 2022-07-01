import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
#cuurent working directory
location = os.getcwd()

def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    service_obj = Service(r"C:\Users\davud\Desktop\SeleniumD\chromedriver.exe")

    # download file in desired location
    preferences = {"download.default_directory": location}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences)
    driver = webdriver.Chrome(service=service_obj, options=ops)
    return driver

def edge_setup():
    from selenium.webdriver.edge.service import Service
    service_obj = Service(r"C:\Users\davud\Desktop\SeleniumD\msedgedriver.exe")

    # download file in desired location
    preferences = {"download.default_directory": location}
    ops = webdriver.EdgeOptions()
    ops.add_experimental_option("prefs", preferences)
    driver = webdriver.Edge(service=service_obj, options=ops)
    return driver

def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    service_obj = Service(r"C:\Users\davud\Desktop\SeleniumD\geckodriver.exe")

    # download file in desired location

    ops = webdriver.FirefoxOptions()
    #ignoring the window
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/msword")
    ops.set_preference("browser.download.manager.showWhenStarting", False)
    #desired location
    ops.set_preference("browser.download.folderList", 2) #1 desktop 2download 3desired
    ops.set_preference("browser.download.dir", location)

    driver = webdriver.Firefox(service=service_obj, options=ops)
    return driver



driver = chrome_setup()
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
download_button = driver.find_element(By.XPATH, "//tbody/tr[1]/td[5]/a[1]")
download_button.click()



# PDF

def chrome_setup_pdf():
    from selenium.webdriver.chrome.service import Service
    service_obj = Service(r"C:\Users\davud\Desktop\SeleniumD\chromedriver.exe")

    # download file in desired location
    preferences = {"download.default_directory": location, "plugins.always.open.pdf_externally":True}

    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences)
    driver = webdriver.Chrome(service=service_obj, options=ops)
    return driver



def edge_setup_pdf():
    from selenium.webdriver.edge.service import Service
    service_obj = Service(r"C:\Users\davud\Desktop\SeleniumD\msedgedriver.exe")

    # download file in desired location and pdf bug have an open bug
    preferences = {"download.default_directory": location}
    preferences = {"download.default_directory": location, "plugins.always.open.pdf_externally": True}
    ops = webdriver.EdgeOptions()
    ops.add_experimental_option("prefs", preferences)
    driver = webdriver.Edge(service=service_obj, options=ops)
    return driver



def firefox_setup_pdf():
    from selenium.webdriver.firefox.service import Service
    service_obj = Service(r"C:\Users\davud\Desktop\SeleniumD\geckodriver.exe")

    # download file in desired location

    ops = webdriver.FirefoxOptions()
    #ignoring the window
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf") #check mime type (sitepoint.com/mime-types-complete-list/)
    ops.set_preference("browser.download.manager.showWhenStarting", False)
    #desired location
    ops.set_preference("browser.download.folderList", 2) #1 desktop 2download 3desired
    ops.set_preference("browser.download.dir", location)
    ops.set_preference("pdfjs.disabled", True) #pdf

    driver = webdriver.Firefox(service=service_obj, options=ops)
    return driver

pdf_file = driver.find_element(By.XPATH)