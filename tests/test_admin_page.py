import time
import pytest

from admin_page import AdminPage
from find_element import FindElement
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
    open_page_product = FindElement(browser)
    add_product_item = AddProduct(browser)
    open_page_product.find_elements_by_id("column-left")
    time.sleep(1)
    list_by_id = ["button-menu", "menu-catalog"]
    for element in list_by_id:
        open_page_product.find_and_click_element_by_id(element)
        time.sleep(1)

    open_page_product.find_and_click_element_by_link_text("Products")
    time.sleep(1)
    open_page_product.find_elements_by_class_name("float-end")
    time.sleep(1)
    open_page_product.find_and_click_element_by_css_selector("[aria-label='Add New']")
    time.sleep(1)
    add_product_item.add_new_product_item("XIAOMI 10")


def test_remove_product_item(browser):
    open_admin_page(browser)
    open_page_product = FindElement(browser)
    remove_product_item = AddProduct(browser)
    open_page_product.find_elements_by_id("column-left")
    time.sleep(1)
    list_by_id = ["button-menu", "menu-catalog"]
    for element in list_by_id:
        open_page_product.find_and_click_element_by_id(element)
        time.sleep(1)

    open_page_product.find_and_click_element_by_link_text("Products")
    time.sleep(1)
    open_page_product.find_elements_by_class_name("float-end")
    time.sleep(1)
    remove_product_item.remove_product_item(select_item_text="[value='42']")


def test_add_new_user(browser):
    open_register_page = FindElement(browser)
    add_new_user = RegisterNewUser(browser)

    open_register_page.open("https://demo.opencart.com/")
    time.sleep(1)
    browser.maximize_window()
    open_register_page.find_elements_by_class_name("fas fa-caret-down")
    time.sleep(1)
    open_register_page.find_elements_by_name("My Account")
    time.sleep(1)
    open_register_page.find_and_click_element_by_xpath("//span[text()='My Account']")
    time.sleep(1)
    open_register_page.find_elements_by_class_name("dropdown-menu dropdown-menu-right show")
    open_register_page.find_elements_by_name("Register")
    open_register_page.find_and_click_element_by_xpath("//a[text()='Register']")
    time.sleep(1)
    add_new_user.add_user_data("Zinka", "Lastova", "fivefeo@mail.ru", "1234")


@pytest.mark.parametrize("currency", ['€ Euro', '£ Pound Sterling', '$ US Dollar'])
def test_change_currency(browser, currency):
    change_currency = FindElement(browser)
    change_currency.open("https://demo.opencart.com/")
    browser.maximize_window()
    change_currency.find_elements_by_id("form-currency")
    time.sleep(1)
    change_currency.find_and_click_element_by_id("form-currency")
    time.sleep(1)
    change_currency.find_elements_by_css_selector("[class='dropdown-menu show']")
    time.sleep(1)
    change_currency.find_and_click_element_by_xpath(f"//a[text()='{currency}']")
