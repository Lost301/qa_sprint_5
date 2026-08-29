from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from locators import Locators as L
from tests.helpers import login, register_user, wait_click


def test_login_from_main_button(driver, base_url):
    email, password = register_user(driver, base_url)
    driver.get(base_url)
    wait_click(driver, L.LOGIN_MAIN)
    login(driver, email, password)
    WebDriverWait(driver, 10).until(ec.url_to_be(base_url))


def test_login_from_personal_account_button(driver, base_url):
    email, password = register_user(driver, base_url)
    driver.get(base_url)
    wait_click(driver, L.PERSONAL_ACCOUNT)
    login(driver, email, password)
    WebDriverWait(driver, 10).until(ec.url_to_be(base_url))


def test_login_link_from_registration(driver, base_url):
    driver.get(base_url + "register")
    wait_click(driver, L.LOGIN_FROM_REGISTER)
    assert "/login" in driver.current_url


def test_login_link_from_password_recovery(driver, base_url):
    driver.get(base_url + "login")
    wait_click(driver, L.FORGOT_PASSWORD)
    wait_click(driver, L.LOGIN_FROM_FORGOT)
    assert "/login" in driver.current_url
