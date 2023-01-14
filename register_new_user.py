import time

from selenium.webdriver.common.by import By


class RegisterNewUser:

    def __init__(self, browser):
        self.browser = browser

    def add_user_data(self, firstname, lastname, email, password):

        self.browser.find_element(By.NAME, "firstname").clear()
        self.browser.find_element(By.NAME, "firstname").send_keys(firstname)

        self.browser.find_element(By.NAME, "lastname").clear()
        self.browser.find_element(By.NAME, "lastname").send_keys(lastname)

        self.browser.find_element(By.NAME, "email").clear()
        self.browser.find_element(By.NAME, "email").send_keys(email)

        self.browser.find_element(By.ID, "input-password").clear()
        self.browser.find_element(By.ID, "input-password").send_keys(password)

        self.browser.find_element(By.NAME, "agree").click()
        self.browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
