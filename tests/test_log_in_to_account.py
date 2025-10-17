from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Credentials
from locators import *
from curl import *


class TestLogInToAccount:
    def test_log_in_using_the_log_in_to_account_button(self, driver):
        driver.get(main_site)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                MainPageLocators.LOGIN_IN_TO_ACCOUNT_BUTTON
            )
        )

        driver.find_element(*MainPageLocators.LOGIN_IN_TO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        )
        email = Credentials.email
        password = Credentials.password
        driver.find_element(*LoginPageLocators.EMAIL).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        assert driver.current_url == main_site

    def test_log_in_to_the_account_through_the_personal_cabinet_button(self, driver):
        driver.get(main_site)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCAUNT_BUTTON)
        )

        driver.find_element(*MainPageLocators.PERSONAL_ACCAUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        )
        email = Credentials.email
        password = Credentials.password
        driver.find_element(*LoginPageLocators.EMAIL).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        assert driver.current_url == main_site

    def test_log_in_to_account_via_the_button_in_the_registration_form(self, driver):
        driver.get(registr_page)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegisterPageLocators.LOGIN_LINK)
        )

        driver.find_element(*RegisterPageLocators.LOGIN_LINK).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        )
        email = Credentials.email
        password = Credentials.password
        driver.find_element(*LoginPageLocators.EMAIL).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        assert driver.current_url == main_site

    def test_log_in_to_account_the_button_in_the_password_recovery_form(self, driver):
        driver.get(forgot_password)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ForgotPasswordLocators.LOG_LINK)
        )

        driver.find_element(*ForgotPasswordLocators.LOG_LINK).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        )
        email = Credentials.email
        password = Credentials.password
        driver.find_element(*LoginPageLocators.EMAIL).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        assert driver.current_url == main_site
