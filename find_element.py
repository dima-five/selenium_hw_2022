from selenium.webdriver.common.by import By


class FindElement:
    def __init__(self, browser):
        self.browser = browser

    def open(self, url):
        self.browser.get(url)

    def find_elements_by_id(self, expected_text):
        self.browser.find_elements(By.ID, expected_text)

    def find_elements_by_name(self, expected_text):
        self.browser.find_elements(By.NAME, expected_text)

    def find_elements_by_class_name(self, expected_text):
        self.browser.find_elements(By.CLASS_NAME, expected_text)

    def find_elements_by_css_selector(self, expected_text):
        self.browser.find_elements(By.CSS_SELECTOR, expected_text)

    def find_elements_by_link_text(self, expected_text):
        self.browser.find_elements(By.LINK_TEXT, expected_text)

    def verify_title_text(self, expected_text):
        assert expected_text in self.browser.title

    def find_and_click_element_by_id(self, expected_text):
        self.browser.find_element(By.ID, expected_text).click()

    def find_and_click_element_by_class_name(self, expected_text):
        self.browser.find_element(By.CLASS_NAME, expected_text).click()

    def find_and_click_element_by_link_text(self, expected_text):
        self.browser.find_element(By.LINK_TEXT, expected_text).click()

    def find_and_click_element_by_css_selector(self, expected_text):
        self.browser.find_element(By.CSS_SELECTOR, expected_text).click()

    def find_and_click_element_by_name(self, expected_text):
        self.browser.find_element(By.NAME, expected_text).click()

    def find_and_click_element_by_xpath(self, expected_text):
        self.browser.find_element(By.XPATH, expected_text).click()
