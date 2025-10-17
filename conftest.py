import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from curl import *
from helper import GenerateCredentials
from data import Credentials
from locators import *


@pytest.fixture
# Фикстура для драйвера
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1200, 600")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
