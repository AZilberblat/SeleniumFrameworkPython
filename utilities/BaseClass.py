from selenium.webdriver.support import expected_conditions as EC

import pytest
import inspect
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifyLinkPresenceBySelector(self, text):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, text)))

    def verifyLinkPresenceByName(self, text):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.NAME, text)))

    def verifyLinkPresenceByText(self, text):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, text)))

    def verifyLinkPresenceByTag(self, text):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, text)))


    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger
