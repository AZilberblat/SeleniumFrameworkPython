import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from testData.HomePageData import HomePageData


class TestTwo(BaseClass):

    def test_signin(self, getData):
        log = self.getLogger()
        log.info("Sign in form:")
        homepage = HomePage(self.driver)
        userName = getData["username"]
        log.info("UserName: " + getData["username"])
        homepage.signin_button().click()

        self.verifyLinkPresenceByName("loginusername")

        email = homepage.getUsername().send_keys(getData["email"])
        log.info("Email: " + getData["email"])

        password = homepage.getPassword().send_keys(getData["password"])
        log.info("Password: " + getData["password"])

        signinButton = homepage.getLoginButton().click()

        self.verifyLinkPresenceByText(userName)

        signinName = str(homepage.getSigninName().text)
        signinName = signinName.replace("היי,", "")
        log.info("Singed in Username: " +signinName)

        assert signinName in userName

    @pytest.fixture(params=HomePageData.test_login_data)
    def getData(self, request):
        return request.param