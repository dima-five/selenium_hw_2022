from selenium.webdriver.common.by import By


def test_title_page_opencart(browser):
    browser.get("https://demo.opencart.com/")
    list_by_id = ["logo", "menu", "cart"]
    for element in list_by_id:
        browser.find_elements(By.ID, element)
    list_by_name = ["cart__grup", "login"]
    for element in list_by_name:
        browser.find_elements(By.ID, element)


def test_marketplace_page_opencart(browser):
    browser.get("https://www.opencart.ru/modules/")
    # verify_title_text(expected_text="Модули opencart")
    assert "Модули opencart" in browser.title
    browser.find_elements(By.ID, "product-category")
    list_by_name = ["blog-page", "list-group"]
    for element in list_by_name:
        browser.find_elements(By.ID, element)
    browser.find_elements(By.CSS_SELECTOR, "button[type=button-filter]")


def test_product_card_page_opencart(browser):
    browser.get("https://www.opencart.ru/"
                        "amigration-perenos-dannyh-s-opencart-15-na-opencart-2-modul-migracii-osnovnyh-dannyh-301")
    assert "Купить A-migration – перенос данных с OpenCart 1.5. * на OpenCart 2. * - модуль миграции основных данных" \
           in browser.title
    browser.find_elements(By.ID, "product-product")
    list_by_name = ["product__title", "rating__svg", "star-no", "purchase__block"]
    for element in list_by_name:
        browser.find_elements(By.ID, element)
    browser.find_elements(By.CSS_SELECTOR, "button[type=button-cart]")


def test_login_page_user_opencart(browser):
    browser.get("https://www.opencart.ru/login/")
    assert "Авторизация" in browser.title
    browser.find_elements(By.ID, "account-login")
    browser.find_elements(By.NAME, "breadcrumb blog")
    browser.find_elements(By.LINK_TEXT, "Личный Кабинет")
    list_by_name = ["customer_form", "login__input-email"]
    for element in list_by_name:
        browser.find_elements(By.NAME, element)
    browser.find_elements(By.CSS_SELECTOR, "button[type=submit]")


def test_register_user_page_opencart(browser):
    browser.get("https://www.opencart.ru/register/")
    assert "Регистрация" in browser.title
    list_by_id = ["account-register", "customer_form"]
    for element in list_by_id:
        browser.find_elements(By.ID, element)
    browser.find_elements(By.LINK_TEXT, "Основные данные")
    list_by_name = ["firstname", "lastname"]
    for element in list_by_name:
        browser.find_elements(By.NAME, element)
    browser.find_elements(By.CSS_SELECTOR, "button[type=submit]")
