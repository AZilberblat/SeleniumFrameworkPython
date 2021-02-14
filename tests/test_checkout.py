import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from testData.HomePageData import HomePageData

import  time

class TestThree(BaseClass):

    def test_checkout(self):
        log = self.getLogger()
        log.info("Checkout Page:")
        homepage = HomePage(self.driver)
        checkout = CheckoutPage(self.driver)
        items = homepage.getCartItems()


        for i in range(0, 3):
            items[i].click()
            time.sleep(1)


        homepage.getCheckoutButton().click()
        self.verifyLinkPresenceByTag("bdi")

        prices = checkout.getPrices()
        #log.info("Prices: " + " ".join(prices))
        capturedPrices = []
        for i in prices:
            capturedPrices.append(i.text.replace("₪", ""))
        finalPrices = [float(i) for i in capturedPrices]
        pricesList = ",".join(capturedPrices)
        log.info("Prices: " + pricesList)
        discount = 0
        if (sum(finalPrices[0:-1]) == finalPrices[-1]):
            discount = 0
            log.info("Final Price: " + str(finalPrices[-1]))
            log.info("Discount Is: " + str(discount))

        elif (sum(finalPrices[0:-2]) == finalPrices[-2]):
            discount = finalPrices[-2] - finalPrices[-1]
            log.info("Price Before Discount: " + str(finalPrices[-2]))
            log.info("Discount Is: " + str(discount))
            log.info("Prices After Discount: " + str(finalPrices[-1]))



