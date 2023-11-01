from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    FULL_NAME_FIELD = (By.ID, 'userName')
    EMAIL_FIELD = (By.ID, 'userEmail')
    CURRENT_ADDRESS_FIELD = (By.XPATH, '//textarea[@id = "currentAddress"]')
    PERMANENT_ADDRESS_FIELD = (By.XPATH, '//textarea[@id = "permanentAddress"]')
    SUBMIT_BUTTON = (By.ID, 'submit')

    CREATED_FULL_NAME = (By.ID, 'name')
    CREATED_EMAIL = (By.ID, 'email')
    CREATED_CURRENT_ADDRESS = (By.XPATH, '//p[@id = "currentAddress"]')
    CREATED_PERMANENT_ADDRESS = (By.XPATH, '//p[@id = "permanentAddress"]')

class CheckBoxPageLocators:
    EXPEND_ALL_BUTTON = (By.XPATH, '//button[@title="Expand all"]')
    CHECKBOX_LIST = (By.XPATH, '//span[@class="rct-text"]')
    CHECKED_CHECKBOXES = (By.XPATH, '//*[@class="rct-icon rct-icon-check"]')
    TITLE_CHECKBOX = './../following-sibling::span[@class="rct-title"]'
    OUTPUT_RESULTS  = (By.XPATH, '//span[@class="text-success"]')