from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from data import generate_credentials
from locators import Locators as L
from tests.helpers import wait_click


def test_successful_registration(driver, base_url):
    email, password = generate_credentials()
    driver.get(base_url + "register")
    driver.find_element(*L.NAME).send_keys("Test User")
    driver.find_element(*L.REGISTER_EMAIL).send_keys(email)
    driver.find_element(*L.PASSWORD).send_keys(password)
    wait_click(driver, L.REGISTER_SUBMIT)
    WebDriverWait(driver, 10).until(ec.url_contains("/login"))


def test_registration_invalid_short_password(driver, base_url):
    email, _ = generate_credentials()
    driver.get(base_url + "register")
    driver.find_element(*L.NAME).send_keys("Test User")
    driver.find_element(*L.REGISTER_EMAIL).send_keys(email)
    driver.find_element(*L.PASSWORD).send_keys("12345")
    wait_click(driver, L.REGISTER_SUBMIT)
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located(L.INVALID_PASSWORD))
