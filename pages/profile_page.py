import logging

from selenium.webdriver.common.by import By

from constants.profile_page_constants import ProfilePageConstants
from helpers.base_helpers import BaseHelpers


class ProfilePage(BaseHelpers):
    """Store of helpers related to Profile page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = ProfilePageConstants
        self.log = logging.getLogger(__name__)

    def edit_personal_data(self, first_name='', last_name='', web_site='', about_text=''):
        """Editing personal data in 'My Profile' page"""
        # Change fields: first name, last name, website and about_yourself by deleting old information and fill new data
        self.wait_and_fill_input_field(locator_type=By.XPATH, locator=self.constants.FIRST_NAME_INPUT_FIELD_XPATH, text=first_name)
        self.wait_and_fill_input_field(locator_type=By.XPATH, locator=self.constants.LAST_NAME_INPUT_FIELD_XPATH, text=last_name)
        self.wait_and_fill_input_field(locator_type=By.XPATH, locator=self.constants.WEB_SITE_INPUT_FIELD_XPATH, text=web_site)
        self.wait_and_fill_input_field(locator_type=By.XPATH, locator=self.constants.ABOUT_INPUT_FIELD_XPATH, text=about_text)
        self.log.info("Changed personal data")

        # Save changes
        self.wait_and_click(locator_type=By.XPATH, locator=self.constants.SAVE_BUTTON_XPATH)
        self.log.info("Save changes")

        # Verify changes by checking success message
        success_message = self.wait_until_element_find(locator_type=By.XPATH, locator=self.constants.SUCCESS_MESSAGE_XPATH)
        assert success_message.text == self.constants.SUCCESS_MESSAGE_TEXT
        self.log.info("Verified changes about changing personal data")
