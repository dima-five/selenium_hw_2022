import time

from selenium.webdriver.common.by import By


def test_title_page_opencart(browser):
    browser.get("https://www.opencart.ru")
    browser.find_element(By.ID, "logo")
    browser.find_element(By.ID, "menu")
    browser.find_element(By.ID, "cart")
    browser.find_elements(By.CLASS_NAME, "cart__grup")
    browser.find_elements(By.CLASS_NAME, "login")


def test_marketplace_page_opencart(browser):
    browser.get("https://www.opencart.ru/modules/")
    assert "Модули opencart" in browser.title
    browser.find_elements(By.ID, "product-category")
    browser.find_elements(By.CLASS_NAME, "blog-page")
    browser.find_elements(By.CLASS_NAME, "list-group")
    browser.find_elements(By.CSS_SELECTOR, "button[type=button-filter]")


def test_product_card_page_opencart(browser):
    browser.get("https://www.opencart.ru/"
                "amigration-perenos-dannyh-s-opencart-15-na-opencart-2-modul-migracii-osnovnyh-dannyh-301")
    assert "Купить A-migration – перенос данных с OpenCart 1.5. * на OpenCart 2." \
           " * - модуль миграции основных данных" in browser.title
    browser.find_elements(By.ID, "product-product")
    browser.find_elements(By.CLASS_NAME, "product__title")
    browser.find_elements(By.CLASS_NAME, "rating__svg")
    browser.find_elements(By.CLASS_NAME, "star-no")
    browser.find_elements(By.CLASS_NAME, "purchase__block")
    browser.find_elements(By.CSS_SELECTOR, "button[type=button-cart]")


def test_login_page_user_opencart(browser):
    browser.get("https://www.opencart.ru/login/")
    assert "Авторизация" in browser.title
    browser.find_elements(By.ID, "account-login")
    browser.find_elements(By.CLASS_NAME, "breadcrumb blog")
    browser.find_elements(By.LINK_TEXT, "Личный Кабинет")
    browser.find_elements(By.ID, "customer_form")
    browser.find_elements(By.ID, "login__input-email")
    browser.find_elements(By.CSS_SELECTOR, "button[type=submit]")


def test_register_user_page_opencart(browser):
    browser.get("https://www.opencart.ru/register/")
    assert "Регистрация" in browser.title
    browser.find_elements(By.ID, "account-register")
    browser.find_elements(By.ID, "customer_form")
    browser.find_elements(By.LINK_TEXT, "Основные данные")
    browser.find_elements(By.NAME, "firstname")
    browser.find_elements(By.NAME, "lastname")
    browser.find_elements(By.CSS_SELECTOR, "button[type=submit]")
