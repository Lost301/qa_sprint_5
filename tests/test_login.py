from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from data import BASE_URL
from helpers import login, register_user, wait_click
from locators import Locators as L


class TestLogin:
    def test_login_from_main_button(self, driver):
        email, password = register_user(driver)
        driver.get(BASE_URL)
        wait_click(driver, L.LOGIN_MAIN)
        login(driver, email, password)

        assert WebDriverWait(driver, 10).until(ec.url_to_be(BASE_URL))

    def test_login_from_personal_account_button(self, driver):
        email, password = register_user(driver)
        driver.get(BASE_URL)
        wait_click(driver, L.PERSONAL_ACCOUNT)
        login(driver, email, password)

        assert WebDriverWait(driver, 10).until(ec.url_to_be(BASE_URL))

    def test_login_link_from_registration(self, driver):
        driver.get(BASE_URL + "register")
        wait_click(driver, L.LOGIN_FROM_REGISTER)

        assert "/login" in driver.current_url

    def test_login_link_from_password_recovery(self, driver):
        driver.get(BASE_URL + "login")
        wait_click(driver, L.FORGOT_PASSWORD)
        wait_click(driver, L.LOGIN_FROM_FORGOT)

        assert "/login" in driver.current_url
