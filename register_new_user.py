import time

from selenium.webdriver.common.by import By

from find_element import FindElement


class RegisterNewUser:

    def __init__(self, browser):
        self.browser = browser

    def add_user_data(self, firstname, lastname, email, password):

        add_user_data = FindElement(self.browser)
        self.browser.find_element(By.NAME, "firstname").clear()
        self.browser.find_element(By.NAME, "firstname").send_keys(firstname)

        self.browser.find_element(By.NAME, "lastname").clear()
        self.browser.find_element(By.NAME, "lastname").send_keys(lastname)

        self.browser.find_element(By.NAME, "email").clear()
        self.browser.find_element(By.NAME, "email").send_keys(email)

        self.browser.find_element(By.ID, "input-password").clear()
        self.browser.find_element(By.ID, "input-password").send_keys(password)

        add_user_data.find_and_click_element_by_name(expected_text="agree")
        add_user_data.find_and_click_element_by_css_selector(expected_text='[type="submit"]')
