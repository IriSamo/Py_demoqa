import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.set_window_size(1400, 700)
    # driver.maximize_window()
    yield driver
    driver.quit()