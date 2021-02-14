from selenium.webdriver.common.by import By

class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    prices = (By.TAG_NAME, "bdi")


    def getPrices(self):
        return self.driver.find_elements(*CheckoutPage.prices)

