import csv
import undetected_chromedriver as uc


class Login:
    def setup_method(self, method):
        self.driver = uc.Chrome()
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
        self.driver.find_element_by_id("email").click()
        self.driver.send_keys(email)
        self.driver.find_element_by_id("password").click()
        self.driver.send_keys(password)
        self.driver.find_element_by_css_selector("button.chakra-button").click()

