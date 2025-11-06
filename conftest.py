import pytest

from selenium import  webdriver
driver=webdriver.Chrome()
@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()
