from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Credentials
from locators import *
from curl import *


class TestTransferToPersonalAccount:
    def test_transfer_to_personal_account(self, driver):
        driver.get(login_page)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        )
        email = Credentials.email
        password = Credentials.password
        driver.find_element(*LoginPageLocators.EMAIL).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))
        driver.find_element(*MainPageLocators.PERSONAL_ACCAUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(profile))

        assert driver.current_url == profile
