import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select as SE
from selenium.webdriver import ActionChains as AC

service_obj = Service(r"C:\Users\davud\Desktop\SeleniumD\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://testautomationpractice.blogspot.com/')

#First task is to enter "Selenium" in searchbox nad submit the find
input_search = driver.find_element(By.XPATH, "//input[@id='Wikipedia1_wikipedia-search-input']")
input_search.send_keys("Selenium")
submit_search = driver.find_element(By.XPATH, "//input[@type='submit']")
submit_search.click()
time.sleep(5)

#Second task is to capture all a hrefs into links variable and print the length of the links

links = driver.find_elements(By.XPATH, "//div[@class='wikipedia-search-main-container'] //a")
print(len(links))

for link in links:
    print(link.text)

time.sleep(2)

#This for loop is click and open all the links
for link in links:
    link.click()

wID = driver.window_handles
print("---------------------------------")
print("Total number of open links is: ", len(wID))

time.sleep(3)

#this loop provides all web pages titles through window handles
for single_id in wID:
    driver.switch_to.window(single_id)
    print(driver.title)

time.sleep(10)

#this loop select specific site titiles and closes them
for close_id in wID:
    driver.switch_to.window(close_id)
    if driver.title == "Selenium dioxide - Wikipedia" or driver.title == "Selenium disulfide - Wikipedia" \
            or driver.title == "Selenium in biology - Wikipedia":
        driver.close()

#we must go to to main page usind driver window handles [0] so we can click on alert js button
main_page_id = driver.window_handles[0]
driver.switch_to.window(main_page_id)
#javascript alert button
time.sleep(5)
alert_button = driver.find_element(By.XPATH, "//button[@onclick='myFunction()']")
alert_button.click()
time.sleep(1)

print("\n\n-------------------------")
#switch to alert window and accept using window accept
alert_window = driver.switch_to.alert
print(alert_window.text)
alert_window.accept()

driver.switch_to.window(main_page_id)

#Date picker on calenar

calendar_input = driver.find_element(By.ID, "datepicker")
calendar_input.click()
time.sleep(1)

date_picer = driver.find_element(By.XPATH, "//a[text() = '24']")
date_picer.click()

time.sleep(1)

#Import select class and use SE class with driver find element
#select by value,index or visible text

select_a_speed_input = SE(driver.find_element(By.ID, "speed"))
select_a_speed_input.select_by_visible_text("Faster")

time.sleep(1.5)

select_a_file_input = SE(driver.find_element(By.ID, "files"))
select_a_file_input.select_by_value("2")

time.sleep(1.5)

select_a_number_input = SE(driver.find_element(By.ID, "number"))
select_a_number_input.select_by_index("4")

time.sleep(1.5)

select_a_product_input = SE(driver.find_element(By.ID, "products"))
select_a_product_input.select_by_value("Apple")

time.sleep(1.5)

select_a_animal_input = SE(driver.find_element(By.ID, "animals"))
select_a_animal_input.select_by_visible_text("Cat")

time.sleep(2)

#Volonteer section (iFrame)

driver.switch_to.frame("frame-one1434677811")

driver.find_element(By.ID, "RESULT_TextField-1").send_keys("Davud")
driver.find_element(By.ID, "RESULT_TextField-2").send_keys("Gobeljic")
driver.find_element(By.ID, "RESULT_TextField-3").send_keys("062519555")
driver.find_element(By.ID, "RESULT_TextField-4").send_keys("Bosnia")
driver.find_element(By.ID, "RESULT_TextField-5").send_keys("Sarajevo")
driver.find_element(By.ID, "RESULT_TextField-6").send_keys("davud.gobeljic@gmail.com")

#radiobutton male or female and days
radiobutton_male_or_female = driver.find_elements(By.ID, "RESULT_RadioButton-7_0")
print(len(radiobutton_male_or_female))

select_male_radiobutton = driver.find_element(By.XPATH, "//label[@for='RESULT_RadioButton-7_0']")
select_male_radiobutton.click()


select_friday = driver.find_element(By.XPATH, "//label[@for='RESULT_CheckBox-8_5']")
select_friday.click()

time.sleep(2)
# turn back from iframe content to default content

driver.switch_to.default_content()
#Double click area

double_click_input = driver.find_element(By.XPATH, "//input[@id='field1']")
double_click_input.clear()
double_click_input.send_keys("Sta imaaaaa")
time.sleep(2)

copy_text_button = driver.find_element(By.XPATH, "//button[normalize-space()='Copy Text']")

#to perform double click we must import Class from webdriver =  from selenium.webdriver import ActionChains

ac_obj = AC(driver)

ac_obj.double_click(copy_text_button).perform()

#to perform drag and drop we must indetify web element and use comand drag and drop which recives two parameters

drag = driver.find_element(By.ID, "draggable")

drop = driver.find_element(By.ID, "droppable")
time.sleep(1)

ac_obj.drag_and_drop(drag, drop).perform()


#second drag and drop section with two users and trash
time.sleep(1)

mr_john = driver.find_element(By.XPATH, '//*[@id="gallery"]/li[1]')
mery = driver.find_element(By.XPATH, '//*[@id="gallery"]/li[2]')

trash_drop = driver.find_element(By.ID, "trash")

ac_obj.drag_and_drop(mr_john, trash_drop).perform()
ac_obj.drag_and_drop(mery, trash_drop).perform()

time.sleep(1)

#take mery out of trash
trash_mery = driver.find_element(By.XPATH, '//*[@id="trash"]/ul/li[2]')

gallery = driver.find_element(By.ID, "gallery")
time.sleep(3)

ac_obj.drag_and_drop(trash_mery, gallery).perform()

#scroll down till the end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")


# table
print("----------------T A B L E----------------")

table_row = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))
table_col = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr/th"))

for r in range(2, table_row + 1):
    for c in range(1, table_col + 1):
        dt = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(dt, end=" ")
    print()



print("-------------------Conditional TABLE------------------------")



for row in range(2, table_row + 1):
    authorName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(row)+"]/td[2]").text
    if authorName == 'Mukesh':
        bookName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(row)+"]/td[1]").text
        subject = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(row)+"]/td[3]").text
        print('Author : ', authorName, '\n Book name is: ', bookName, 'with subject of: ', subject)