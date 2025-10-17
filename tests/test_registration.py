from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helper import GenerateCredentials
from locators import *
from curl import *


class TestRegistrationWitNewCredentails:
    def test_successful_registration(self, driver):
        driver.get(registr_page)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegisterPageLocators.REG_BUTTON)
        )
        name = GenerateCredentials.generate_name()
        email = GenerateCredentials.generate_email()
        password = GenerateCredentials.generate_password()
        driver.find_element(*RegisterPageLocators.NAME).send_keys(name)
        driver.find_element(*RegisterPageLocators.EMAIL).send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD).send_keys(password)
        driver.find_element(*RegisterPageLocators.REG_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.url_changes(registr_page)  # ждём, пока URL изменится
        )
        assert driver.current_url == login_page


class TestRegisrationInvalidPassword:
    def test_invalid_password(self, driver):
        driver.get(registr_page)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegisterPageLocators.REG_BUTTON)
        )
        name = GenerateCredentials.generate_name()
        email = GenerateCredentials.generate_email()
        password = GenerateCredentials.generate_password()
        password = GenerateCredentials.generate_invalid_password()
        driver.find_element(*RegisterPageLocators.NAME).send_keys(name)
        driver.find_element(*RegisterPageLocators.EMAIL).send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD).send_keys(password)

        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegisterPageLocators.PASSWORD_ERROR)
        )
        assert error_message.text == "Некорректный пароль"
