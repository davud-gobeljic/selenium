import pytest
from selenium import webdriver
from pageObjects import LoginPage
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig as RF
from utilities.costumLogger import LogGen as LG


class Test_001_Login:
    baseURL = RF.getApplicationURL()
    username = RF.getApplicationUserEmail()
    password = RF.getApplicationPassword()

    logger = LG.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("********** Test_001_Login *********")
        self.logger.info("********** Veryfying Home Page Title *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("********** Home Page Title test is passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshoots\\" + "test_homePage_title.jpg")
            self.driver.close()
            self.logger.error("********** Home Page Title test is failed *********")
            assert False





    def test_login(self, setup):
        self.logger.info("********** Login test is started *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogIn()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("********** LOGIN test is passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshoots\\" + "tst.jpg")
            self.driver.close()
            self.logger.error("********** LOGIN test is failed *********")
            assert False


