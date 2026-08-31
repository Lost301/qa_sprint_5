from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from data import DataGenerator, Urls
from locators import Locators as L

def wait_click(driver, locator):
    element = WebDriverWait(driver, 10).until(ec.element_to_be_clickable(locator))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    try: element.click()
    except ElementClickInterceptedException: driver.execute_script("arguments[0].click();", element)

def register_user(driver):
    email, password = DataGenerator.generate_credentials()
    driver.get(Urls.BASE_URL + "register")
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located(L.NAME)).send_keys("Test User")
    driver.find_element(*L.REGISTER_EMAIL).send_keys(email)
    driver.find_element(*L.PASSWORD).send_keys(password)
    wait_click(driver, L.REGISTER_SUBMIT)
    WebDriverWait(driver, 10).until(ec.url_contains("/login"))
    return email, password

def login(driver, email, password):
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located(L.LOGIN_EMAIL)).send_keys(email)
    driver.find_element(*L.PASSWORD).send_keys(password)
    wait_click(driver, L.LOGIN_SUBMIT)
