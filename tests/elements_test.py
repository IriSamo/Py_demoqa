from pages.elements_page import TextBoxPage
from pages.elements_page import CheckBoxPage


class TestTextBox:

    def test_text_box(self, driver):
        text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
        text_box_page.open()
        full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
        output_full_name, output_email, output_current_address, output_permanent_address = text_box_page.check_filled_form()

        assert full_name == output_full_name
        assert email == output_email
        assert current_address == output_current_address
        assert permanent_address == output_permanent_address


class TestCheckBox:

    def test_check_box(self, driver):
        check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
        check_box_page.open()
        check_box_page.expand_all_checkboxes()
        check_box_page.check_random_checkboxes()
        input_checkboxes = check_box_page.get_checked_checkboxes()
        output_results = check_box_page.get_output_results()
        assert input_checkboxes == output_results
