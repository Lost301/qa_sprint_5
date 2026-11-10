from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from data import DataGenerator, Urls
from helpers import wait_click
from locators import Locators as L


class TestRegistration:
    def test_successful_registration(self, driver):
        email, password = DataGenerator.generate_credentials()
        driver.get(Urls.BASE_URL + "register")
        driver.find_element(*L.NAME).send_keys("Test User")
        driver.find_element(*L.REGISTER_EMAIL).send_keys(email)
        driver.find_element(*L.PASSWORD).send_keys(password)
        wait_click(driver, L.REGISTER_SUBMIT)
        assert WebDriverWait(driver, 10).until(ec.url_contains("/login"))

    def test_registration_invalid_short_password(self, driver):
        email, _ = DataGenerator.generate_credentials()
        driver.get(Urls.BASE_URL + "register")
        driver.find_element(*L.NAME).send_keys("Test User")
        driver.find_element(*L.REGISTER_EMAIL).send_keys(email)
        driver.find_element(*L.PASSWORD).send_keys("12345")
        wait_click(driver, L.REGISTER_SUBMIT)
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(L.INVALID_PASSWORD))
