from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    register = (By.LINK_TEXT, "הרשמה")
    singin = (By.LINK_TEXT, "התחברות")
    login = (By.NAME, "login")
    username = (By.NAME, "loginusername")
    password = (By.NAME, "loginpassword")
    signinName = (By.CLASS_NAME, "name")
    items = (By.CSS_SELECTOR, '[name="add-to-cart"]')
    checkout = (By.CSS_SELECTOR, '[class="button green"]')


    def register_button(self):
        return self.driver.find_element(*HomePage.register)

    def signin_button(self):
        return self.driver.find_element(*HomePage.singin)

    def getUsername(self):
        return self.driver.find_element(*HomePage.username)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getLoginButton(self):
        return self.driver.find_element(*HomePage.login)

    def getSigninName(self):
        return self.driver.find_element(*HomePage.signinName)

    def getCartItems(self):
        return self.driver.find_elements(*HomePage.items)

    def getCheckoutButton(self):
        return self.driver.find_element(*HomePage.checkout)

