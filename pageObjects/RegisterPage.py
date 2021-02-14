from selenium.webdriver.common.by import By


class RegisterPage:

    def __init__(self, driver):
        self.driver = driver

    first_name = (By.NAME, "first-name")
    last_name = (By.NAME, "second-name")
    email = (By.NAME, "email")
    password = (By.NAME, "password")
    password_confirm = (By.NAME, "password-confirm")
    date_of_birth = (By.CLASS_NAME, "masked-select-inner")
    confirmButton = (By.CLASS_NAME, "send-register-form")
    checkBox = (By.CSS_SELECTOR, "input:checked")
    endDialog = (By.CSS_SELECTOR, "[class=thank-you_title]")

    def getFirstName(self):
        return self.driver.find_element(*RegisterPage.first_name)

    def getLastName(self):
        return self.driver.find_element(*RegisterPage.last_name)

    def getEmail(self):
        return self.driver.find_element(*RegisterPage.email)

    def getPassword(self):
        return self.driver.find_element(*RegisterPage.password)

    def getPasswordConfirm(self):
        return self.driver.find_element(*RegisterPage.password_confirm)

    def getDateOfBirth(self):
        return self.driver.find_elements(*RegisterPage.date_of_birth)

    def getConfirmButton(self):
        return self.driver.find_element(*RegisterPage.confirmButton)

    def getCheckbox(self):
        return self.driver.find_element(*RegisterPage.checkBox)

    def getDialog(self):
        return self.driver.find_element(*RegisterPage.endDialog)
