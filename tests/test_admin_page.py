import time
import pytest
from selenium.webdriver.common.by import By

from admin_page import AdminPage
from currency_items import CurrencyItem
from product_item import AddProduct
from register_new_user import RegisterNewUser


def open_admin_page(browser):
    admin_page = AdminPage(browser)
    admin_page.open()
    admin_page.input_username("demo")
    time.sleep(1)
    admin_page.input_password("demo")
    time.sleep(1)
    admin_page.submit_login()
    time.sleep(1)


def test_open_admin_page(browser):
    open_admin_page(browser)


def test_add_new_product(browser):
    open_admin_page(browser)
    add_product_item = AddProduct(browser)
    browser.find_elements(By.ID, "column-left")
    time.sleep(1)
    list_by_id = ["button-menu", "menu-catalog"]
    for element in list_by_id:
        browser.find_element(By.ID, element).click()
        time.sleep(1)

    browser.find_element(By.LINK_TEXT, "Products").click()
    time.sleep(1)
    browser.find_elements(By.CLASS_NAME, "float-end")
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, "[aria-label='Add New']").click()
    time.sleep(1)
    add_product_item.add_new_product_item("XIAOMI 10")


def test_remove_product_item(browser):
    open_admin_page(browser)
    remove_product_item = AddProduct(browser)
    browser.find_elements(By.ID, "column-left")
    time.sleep(1)
    list_by_id = ["button-menu", "menu-catalog"]
    for element in list_by_id:
        browser.find_element(By.ID, element).click()
        time.sleep(1)

    browser.find_element(By.LINK_TEXT, "Products").click()
    time.sleep(1)
    browser.find_elements(By.CLASS_NAME, "float-end")
    time.sleep(1)
    remove_product_item.remove_product_item(select_item_text="[value='42']")


def test_add_new_user(browser):
    add_new_user = RegisterNewUser(browser)

    browser.get("https://demo.opencart.com/")
    time.sleep(1)
    browser.maximize_window()
    browser.find_elements(By.CLASS_NAME, "fas fa-caret-down")
    time.sleep(1)
    browser.find_elements(By.NAME, "My Account")
    time.sleep(1)
    browser.find_element(By.XPATH, "//span[text()='My Account']").click()
    time.sleep(1)
    browser.find_elements(By.CLASS_NAME, "dropdown-menu dropdown-menu-right show")
    browser.find_elements(By.NAME, "Register")
    browser.find_element(By.XPATH, "//a[text()='Register']").click()
    time.sleep(1)
    add_new_user.add_user_data("Zinka", "Lastova", "fivefeo@mail.ru", "1234")


@pytest.mark.parametrize("currency", ['€ Euro', '£ Pound Sterling', '$ US Dollar'])
def test_change_currency(browser, currency):
    set_currency = CurrencyItem(browser)

    browser.get("https://demo.opencart.com/")
    browser.maximize_window()
    set_currency.open_currency_dropdown()
    set_currency.set_currency_item(expected_currency=currency)
