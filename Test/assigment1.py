from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select as SE
from selenium.webdriver import ActionChains as AC

service_obj = Service(r"C:\Users\davud\Desktop\SeleniumD\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.dummyticket.com/")
driver.find_element(By.XPATH, "//a[contains(text(),'Buy Ticket')]").click()

radio_buttons = driver.find_elements(By.XPATH, "//ul[@id='checkout-products']/li")


time.sleep(2)
click_something = driver.find_element(By.XPATH, "//input[@id='product_3186']")
click_something.click()

driver.find_element(By.ID, "travname").send_keys("Davud")
driver.find_element(By.ID, "travlastname").send_keys("Gobeljic")


datepicker = driver.find_element(By.XPATH, "//input[@id='dob']")
datepicker.click()

yrSel = SE(driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))
yrSel.select_by_visible_text("2017")
monSel = SE(driver.find_element(By.XPATH, "//select[@aria-label='Select month']"))
monSel.select_by_value("7")
lengthof = driver.find_elements(By.XPATH, "//select[@aria-label='Select month']/option")
print(len(lengthof))

for i in lengthof:
    print(i.text)

time.sleep(5)

for mi in lengthof:
    if mi.text == 'Apr':
        mi.click()
        break


time.sleep(2)


table_date = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
print(table_date)

dateMy = '21'

for date in table_date:
    if date.text == dateMy:
        date.click()
        break

driver.find_element(By.XPATH, "//button[normalize-space()='Done']").click()

input_s_m_f = driver.find_elements(By.XPATH, "//p[@id='sex_field']//span[@class='woocommerce-input-wrapper']/input")
time.sleep(2)

male = driver.find_element(By.XPATH, "//input[@id='sex_1']")
male.click()
travel_type = driver.find_element(By.XPATH, "//input[@id='traveltype_1']")
travel_type.click()
time.sleep(1)
where = driver.find_element(By.XPATH, "//input[@id='fromcity']")
where.send_keys("Sarajevo")
driver.find_element(By.XPATH, "//input[@id='tocity']").send_keys("Wien")

driver.find_element(By.XPATH, "//input[@id='departon']").click()

select_month_dep = SE(driver.find_element(By.XPATH, "//select[@aria-label='Select month']"))
select_month_dep.select_by_visible_text('Aug')

arrival_date = '17'

second_table = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//a")
for o in second_table:
    if o.text == arrival_date:
        o.click()
        break

driver.find_element(By.XPATH, "//span[@id='select2-reasondummy-container']").click()

all_options_possible = driver.find_elements(By.XPATH, "//span[@class='select2-results']/ul/li")
for option in all_options_possible:
    if option.text == "Car rental":
        option.click()

time.sleep(1)
# selectLan = driver.find_element(By.XPATH, "//span[normalize-space()='USD']")
# action = AC(driver)
# action.move_to_element(selectLan)
click_us_dollar = driver.find_element(By.XPATH, "//span[normalize-space()='USD']")
click_us_dollar.click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[normalize-space()='USD']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='USD']").click()

first_price = driver.find_element(By.XPATH, "//li[@class='product-item selected']").text
print("This is price :", first_price)
first_price_final = first_price[-10:]
print("aaaa", first_price_final)



end_price = driver.find_element(By.XPATH, "//table[@class='shop_table woocommerce-checkout-review-order-table']//tfoot/tr[2]/td").text
print(end_price)

if first_price_final == end_price:
    print("Final price is good: ", end_price)
else:
    print("Not good")






# driver.find_element(By.XPATH, "//input[@id='billing_phone']").send_keys("062519555")