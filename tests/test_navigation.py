from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from data import BASE_URL
from helpers import login, register_user, wait_click
from locators import Locators as L

class TestNavigation:
    def test_personal_account_opens(self, driver):
        email, password = register_user(driver); driver.get(BASE_URL + "login"); login(driver, email, password); wait_click(driver, L.PERSONAL_ACCOUNT)
        assert WebDriverWait(driver, 10).until(ec.url_contains("/account"))
    def test_constructor_button_from_account(self, driver):
        email, password = register_user(driver); driver.get(BASE_URL + "login"); login(driver, email, password); wait_click(driver, L.PERSONAL_ACCOUNT); wait_click(driver, L.CONSTRUCTOR)
        assert driver.current_url == BASE_URL
    def test_logo_from_account(self, driver):
        email, password = register_user(driver); driver.get(BASE_URL + "login"); login(driver, email, password); wait_click(driver, L.PERSONAL_ACCOUNT); wait_click(driver, L.LOGO)
        assert driver.current_url == BASE_URL
    def test_logout(self, driver):
        email, password = register_user(driver); driver.get(BASE_URL + "login"); login(driver, email, password); wait_click(driver, L.PERSONAL_ACCOUNT); wait_click(driver, L.LOGOUT)
        assert WebDriverWait(driver, 10).until(ec.url_contains("/login"))
    def test_buns_tab(self, driver):
        driver.get(BASE_URL); wait_click(driver, L.BUNS)
        assert "current" in driver.find_element(*L.BUNS).get_attribute("class")
    def test_sauces_tab(self, driver):
        driver.get(BASE_URL); wait_click(driver, L.SAUCES)
        assert "current" in driver.find_element(*L.SAUCES).get_attribute("class")
    def test_fillings_tab(self, driver):
        driver.get(BASE_URL); wait_click(driver, L.FILLINGS)
        assert "current" in driver.find_element(*L.FILLINGS).get_attribute("class")
