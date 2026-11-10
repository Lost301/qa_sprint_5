import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1440,1000")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(2)
    yield browser
    browser.quit()


