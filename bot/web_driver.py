from seleniumwire.undetected_chromedriver import Chrome
import time
from selenium.webdriver.common.by import By

class WebDriver:
    instance = None

    def __init__(self):


    @staticmethod
    def get_driver():
        if WebDriver.instance is None:
            WebDriver()
        return WebDriver.instance

    def __init__(self):
        if WebDriver.instance is None:
            WebDriver.instance = self