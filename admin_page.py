from selenium.webdriver.common.by import By


class AdminPage:

    path = "/admin"
    url = "https://demo.opencart.com"

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get(self.url + self.path)

    def input_username(self, expected_text):
        self.browser.find_element(By.NAME, "username").clear()
        self.browser.find_element(By.NAME, "username").send_keys(expected_text)

    def input_password(self, expected_text):
        self.browser.find_element(By.NAME, "password").clear()
        self.browser.find_element(By.NAME, "password").send_keys(expected_text)

    def submit_login(self):
        self.browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
