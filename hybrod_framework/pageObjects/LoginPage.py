from selenium.webdriver.common.by import By

class Login:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath  = "//button[normalize-space()='Log in']"
    button_logout_xpath = "//a[normalize-space()='Logout']"


    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogIn(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogOut(self):
        self.driver.find_element(By.XPATH, self.button_logout_xpath).click()
