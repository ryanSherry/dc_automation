import csv
import undetected_chromedriver as uc
import time
from selenium.webdriver.common.by import By

driver = uc.Chrome()

class Login:

    def login(self, open_csv_file):
        csv_reader = open_csv_file
        for row in csv_reader:
            email = row['email']
            password = row['password']
            self.execute_login(self, email, password)
        time.sleep(10000)

    def execute_login(self, email, password):
        driver.get("https://nft.dcuniverse.com/purchase")
        driver.maximize_window()
        driver.implicitly_wait(2)
        driver.find_element(By.PARTIAL_LINK_TEXT, 'LOG').click()
        driver.implicitly_wait(2)
        email_field = driver.find_element('id', 'email')
        email_field.click()
        email_field.send_keys(email)
        password_field = driver.find_element('id', 'password')
        password_field.click()
        password_field.send_keys(password)
        driver.find_element(By.CSS_SELECTOR, 'button.chakra-button.css-1j8c3t3').click()
        driver.switch_to.new_window('window')

