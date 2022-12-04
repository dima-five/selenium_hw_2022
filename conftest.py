import os
import time

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", default="http://192.168.0.116:8081")


@pytest.fixture
def browser(request):
    # Getting different params for run 'pytest'
    _browser = request.config.getoption("--browser")
    _url = request.config.getoption("--url")
    driver = None

    # elif _browser == 'chrome':
    #     driver = webdriver.Chrome(executable_path="C:\\Users\\fivef\\Downloads\\webdrivers\\chromedriver")
    # elif _browser == 'edge':
    #     driver = webdriver.Edge(executable_path="C:\\Users\\fivef\\Downloads\\webdrivers\\msedgedriver")
    # elif _browser == 'yandex':
    #     driver = webdriver.Chrome(executable_path="C:\\Users\\fivef\\Downloads\\webdrivers\\yandexdriver")
    if _browser == 'firefox' or _browser == 'ff':
        driver = webdriver.Firefox(executable_path="C:\\Users\\fivef\\Downloads\\webdrivers\\geckodriver")
    if _browser == 'chrome':
        driver = webdriver.Chrome(executable_path="C:\\Users\\fivef\\Downloads\\webdrivers\\chromedriver")
    yield driver
    time.sleep(2)
    driver.close()


