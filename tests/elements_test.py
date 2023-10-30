import time

from pages.base_page import BasePage


def test_check_structure(driver):
    page = BasePage(driver, 'https://google.com')
    page.open()
    time.sleep(2)
    assert page.get_title() == 'Google'
