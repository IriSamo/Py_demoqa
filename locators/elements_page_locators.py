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
    CHECKBOX_LIST = (By.CLASS_NAME, 'rct-checkbox')
    CHECKED_CHECKBOXES = (By.XPATH, '//*[@class="rct-icon rct-icon-check"]')
    TITLE_CHECKBOX = './../following-sibling::span[@class="rct-title"]'
    RESULT = (By.ID, 'result')
    OUTPUT_RESULTS = (By.CSS_SELECTOR, 'span.text-success')


class RadioButtonPageLocators:
    YES_RADIO_BUTTON = (By.ID, 'yesRadio')
    YES_BUTTON = (By.XPATH, '//input[@id="yesRadio"]/following-sibling::label')
    IMPRESSIVE_RADIO_BUTTON = (By.ID, 'impressiveRadio')
    SELECTED_RADIO_BUTTON = (By.CLASS_NAME, 'text-success')
    NO_RADIO_BUTTON = (By.ID, 'noRadio')