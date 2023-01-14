import time

from selenium.webdriver.common.by import By


class CurrencyItem:
    def __init__(self, browser):
        self.browser = browser

    def open_currency_dropdown(self):
        self.browser.find_elements(By.ID, "form-currency")
        time.sleep(1)
        self.browser.find_element(By.ID, "form-currency").click()

    def set_currency_item(self, expected_currency):
        self.browser.find_elements(By.CSS_SELECTOR, "[class='dropdown-menu show']")
        time.sleep(1)
        self.browser.find_element(By.XPATH, f"//a[text()='{expected_currency}']").click()
