import time

from selenium.webdriver.common.by import By


class AddProduct:
    def __init__(self, browser):
        self.browser = browser

    def add_new_product_item(self, expected_text):
        self.browser.find_element(By.ID, "input-name-1").clear()
        self.browser.find_element(By.ID, "input-name-1").send_keys(expected_text)
        time.sleep(1)
        self.browser.find_element(By.ID, "input-meta-title-1").clear()
        self.browser.find_element(By.ID, "input-meta-title-1").send_keys(expected_text)
        time.sleep(1)
        self.browser.find_element(By.CSS_SELECTOR, "[aria-label='Save']").click()

    def remove_product_item(self, select_item_text=None):

        self.browser.find_element(By.CSS_SELECTOR, select_item_text).click()
        time.sleep(1)
        self.browser.find_element(By.CSS_SELECTOR, "[aria-label='Delete']").click()
