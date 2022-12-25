from find_element import FindElement


def test_title_page_opencart(browser):
    title_page = FindElement(browser)
    title_page.open()
    list_by_id = ["logo", "menu", "cart"]
    for element in list_by_id:
        title_page.find_elements_by_id(element)
    list_by_name = ["cart__grup", "login"]
    for element in list_by_name:
        title_page.find_elements_by_id(element)


def test_marketplace_page_opencart(browser):
    marketplace_page = FindElement(browser)
    marketplace_page.open("https://www.opencart.ru/modules/")
    marketplace_page.verify_title_text(expected_text="Модули opencart")
    marketplace_page.find_elements_by_id("product-category")
    list_by_name = ["blog-page", "list-group"]
    for element in list_by_name:
        marketplace_page.find_elements_by_id(element)
    marketplace_page.find_elements_by_css_selector("button[type=button-filter]")


def test_product_card_page_opencart(browser):
    prod_cart_page = FindElement(browser)
    prod_cart_page.open("https://www.opencart.ru/"
                        "amigration-perenos-dannyh-s-opencart-15-na-opencart-2-modul-migracii-osnovnyh-dannyh-301")
    prod_cart_page.verify_title_text("Купить A-migration – перенос данных с OpenCart 1.5. * на OpenCart 2."
                                     " * - модуль миграции основных данных")
    prod_cart_page.find_elements_by_id("product-product")
    list_by_name = ["product__title", "rating__svg", "star-no", "purchase__block"]
    for element in list_by_name:
        prod_cart_page.find_elements_by_id(element)
    prod_cart_page.find_elements_by_css_selector("button[type=button-cart]")


def test_login_page_user_opencart(browser):
    login_page_user = FindElement(browser)
    login_page_user.open("https://www.opencart.ru/login/")
    login_page_user.verify_title_text("Авторизация")
    login_page_user.find_elements_by_id("account-login")
    login_page_user.find_elements_by_name("breadcrumb blog")
    login_page_user.find_elements_by_link_text("Личный Кабинет")
    list_by_name = ["customer_form", "login__input-email"]
    for element in list_by_name:
        login_page_user.find_elements_by_id(element)
    login_page_user.find_elements_by_css_selector("button[type=submit]")


def test_register_user_page_opencart(browser):
    register_user_page = FindElement(browser)
    register_user_page.open("https://www.opencart.ru/register/")
    register_user_page.verify_title_text("Регистрация")
    list_by_id = ["account-register", "customer_form"]
    for element in list_by_id:
        register_user_page.find_elements_by_id(element)
    register_user_page.find_elements_by_link_text("Основные данные")
    list_by_name = ["firstname", "lastname"]
    for element in list_by_name:
        register_user_page.find_elements_by_name(element)
    register_user_page.find_elements_by_css_selector("button[type=submit]")
