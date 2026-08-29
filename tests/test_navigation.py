from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from locators import Locators as L
from tests.helpers import login, register_user, wait_click


def test_personal_account_opens(driver, base_url):
    email, password = register_user(driver, base_url)
    driver.get(base_url + "login")
    login(driver, email, password)
    wait_click(driver, L.PERSONAL_ACCOUNT)
    WebDriverWait(driver, 10).until(ec.url_contains("/account"))


def test_constructor_and_logo_from_account(driver, base_url):
    email, password = register_user(driver, base_url)
    driver.get(base_url + "login")
    login(driver, email, password)
    wait_click(driver, L.PERSONAL_ACCOUNT)
    wait_click(driver, L.CONSTRUCTOR)
    assert driver.current_url == base_url
    wait_click(driver, L.PERSONAL_ACCOUNT)
    wait_click(driver, L.LOGO)
    assert driver.current_url == base_url


def test_logout(driver, base_url):
    email, password = register_user(driver, base_url)
    driver.get(base_url + "login")
    login(driver, email, password)
    wait_click(driver, L.PERSONAL_ACCOUNT)
    wait_click(driver, L.LOGOUT)
    WebDriverWait(driver, 10).until(ec.url_contains("/login"))


def test_constructor_sections(driver, base_url):
    driver.get(base_url)
    for locator in (L.BUNS, L.SAUCES, L.FILLINGS):
        wait_click(driver, locator)
        assert driver.find_element(*locator).is_displayed()
