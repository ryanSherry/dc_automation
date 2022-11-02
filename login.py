import csv
import undetected_chromedriver as uc


class login:
    def setup_method(self):
        self.driver = uc.Chrome()
        self.vars = {}

    def login(self, open_csv_file):
        csv_reader = open_csv_file
        for row in csv_reader:
            email = row['email']
            password = row['password']
            self.execute_login(self, email, password)
        csv_reader.close()

    def execute_login(self, email, password):
        self.driver.switch_to.new_window('window')
        self.driver.get("https://nft.dcuniverse.com/purchase")
        self.driver.maximize_window()
        self.driver.find_element_by_id("email").click()
        self.driver.send_keys(email)
        self.driver.find_element_by_id("password").click()
        self.driver.send_keys(password)
        self.driver.find_element_by_css_selector("button.chakra-button").click()

