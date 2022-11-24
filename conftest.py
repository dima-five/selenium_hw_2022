import os

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="chrome"
    )

@pytest.fixture
def browser(request):
    _browser = request.config.getoption("--browser")
    driver = None
    if _browser == 'firefox' or _browser == 'ff':
        driver = webdriver.Firefox(executable_path="C:\\Users\\fivef\\Downloads\\webdrivers\\geckodriver")
    elif _browser == 'chrome':
        driver = webdriver.Chrome(executable_path="C:\\Users\\fivef\\Downloads\\webdrivers\\chromedriver")
    elif _browser == 'edge':
        driver = webdriver.Edge(executable_path="C:\\Users\\fivef\\Downloads\\webdrivers\\msedgedriver")
    elif _browser == 'yandex':
        driver = webdriver.Chrome(executable_path="C:\\Users\\fivef\\Downloads\\webdrivers\\yandexdriver")
    yield driver
    driver.close()
