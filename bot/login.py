import csv

from selenium.webdriver.support.wait import WebDriverWait
from seleniumwire.undetected_chromedriver import Chrome
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import proxy_retriever
from web_driver import WebDriver


options = {
     'proxy': {
         'https': 'https://5LV10gaMQN:OIRi7LrM79@185.216.104.1:6001'
     }
}

driver = Chrome(seleniumwire_options=options)

class Login:

    def login(self, open_csv_file):
        csv_reader = open_csv_file
        for row in csv_reader:
            email = row['email']
            password = row['password']
            proxy = row['proxy']
            #options = proxy_retriever.format_proxy(proxy)
            #options['user-agent'] = '{ user-agent=Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}''
            options = Chrome().ChromeOptions
            options.add_argument('--user-agent="Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html"')
            options.add_argument('--ignore-certificate-errors')
            driver = Chrome(seleniumwire_options=options)
            self.execute_login(self, email, password, proxy, driver)
        time.sleep(10000)

    def execute_login(self, email, password, proxy, driver):
        #options = proxy_retriever.format_proxy(proxy)
        #driver = Chrome(seleniumwire_options=options)
        driver.maximize_window()
        driver.get("https://nft.dcuniverse.com/purchase")
        #driver.implicitly_wait(1)
        driver.find_element(By.PARTIAL_LINK_TEXT, 'LOG IN').click()
        #driver.implicitly_wait(1)
        email_field = driver.find_element('id', 'email')
        email_field.click()
        email_field.send_keys(email)
        password_field = driver.find_element('id', 'password')
        password_field.click()
        password_field.send_keys(password)
        wait = WebDriverWait(driver, 3)
        time.sleep(2)
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.chakra-button.css-1j8c3t3')))
        element.click()
        driver.window_new()

