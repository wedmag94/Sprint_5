from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest
from data import Credentials
from locators import *
from curl import *


class TestConstructorNavigation:

    def test_constructor_navigation_buns(self, driver):
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
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorLocators.CONSTRUCTOR)
        )
        driver.find_element(*ConstructorLocators.SAUCES).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorLocators.SAUCES_ACTIVE)
        )

        driver.find_element(*ConstructorLocators.BUNS).click()
        active_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorLocators.BUNS_ACTIVE)
        )

        assert (
            active_element.get_attribute("class")
            == "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"
        )

    def test_constructor_navigation_sauces(self, driver):
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
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorLocators.CONSTRUCTOR)
        )
        driver.find_element(*ConstructorLocators.SAUCES).click()
        active_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorLocators.SAUCES_ACTIVE)
        )

        assert (
            active_element.get_attribute("class")
            == "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"
        )

    def test_constructor_navigation_toppings(self, driver):
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
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorLocators.CONSTRUCTOR)
        )
        driver.find_element(*ConstructorLocators.TOPPINGS).click()
        active_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorLocators.TOPPINGS_ACTIVE)
        )

        assert (
            active_element.get_attribute("class")
            == "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"
        )
