import sys, argparse, csv
import pytest
import time
import json
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Login:
    def setup_method(self, method):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        self.driver = webdriver.Chrome(chrome_options)
        self.vars = {}

    def login(self):
        with open('accounts.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                email = row['email']
                password = row['password']
                #                print(email)
                #                print(password)
                self.execute_login(self, email, password)
            csv_file.close()

    def execute_login(self, email, password):
        self.driver.get("https://nft.dcuniverse.com/purchase")
        self.driver.set_window_size(1634, 914)
        self.driver.find_element(By.ID, "email").click()
        self.driver.send_keys(email)
        self.driver.find_element(By.ID, "password").click()
        self.driver.send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "button.chakra-button").click()