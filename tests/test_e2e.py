from selenium import webdriver
import time
import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.HomePage import HomePage
from pageObjects.RegisterPage import RegisterPage
from testData.RegisterPageData import RegisterPageData

from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    @pytest.mark.userTests
    def test_e2e(self, getData):

        log = self.getLogger()

        homepage = HomePage(self.driver)
        register_page = RegisterPage(self.driver)
        homepage.register_button().click()
        #self.driver.get("https://blend.co.il/register")

        log.info("Filling the Form:")
        # filling form first name
        firstName = register_page.getFirstName().send_keys(getData["firstName"])
        log.info("First name entered: "+getData["firstName"])

        # filling form last name
        lastName = register_page.getLastName().send_keys(getData["lastName"])
        log.info("Last name entered: " + getData["lastName"])

        # filling form email
        email = register_page.getEmail().send_keys(getData["email"])
        log.info("Email entered: " + getData["email"])

        # filling form passwords
        password = register_page.getPassword().send_keys(getData["password"])
        passwordConfirm = register_page.getPasswordConfirm().send_keys(getData["password"])
        log.info("password entered: " + getData["password"])

        # unchecking the box of advertising
        checkbox = register_page.getCheckbox()
        self.driver.execute_script("arguments[0].click()", checkbox)
        log.info("Checkbox unchecked: V")

        # filling the date of birth fields

        yearBox = register_page.getDateOfBirth()
        birth = []

        for test in yearBox:
            test.click()
            birth.append(test.find_element_by_class_name("list").find_elements_by_tag_name("li")[1].text)
            test.find_element_by_class_name("list").find_elements_by_tag_name("li")[1].click()

        log.info("Date of birth: " + str(birth))



        # pressing the register button
        register_page.getConfirmButton().click()

        # checking that registration have been completed

        self.verifyLinkPresenceBySelector("[class=thank-you_title]")

        message = str(register_page.getDialog().text)
        message = message.replace("\n", " ")
        log.info("End of form message " + message)
        assert (message in RegisterPageData.outputs["success"])

        self.driver.refresh()

    @pytest.fixture(params=RegisterPageData.getTestData())
    def getData(self, request):
        return request.param
