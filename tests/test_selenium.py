import time

from selenium.webdriver.common.by import By

def test_hello_world(browser):
    # firefox = webdriver.Firefox(executable_path="C:\\Users\\fivef\\Downloads\\webdrivers\\geckodriver")
    browser.get("https://ya.ru")
    assert "Яндекс" in browser.title
    # firefox.close()


def test_open_opencart_site(browser):
    browser.get("https://www.opencart.ru")


