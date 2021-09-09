import logging

from selenium.webdriver.common.by import By

from constants.registration_and_sign_in_page_constants import RegistrationAndSignInPageConstants
from helpers.base_helpers import BaseHelpers, UserData


class RegistrationAndSignInPage(BaseHelpers):
    """Store of methods related to Registration and Sign In page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.log = logging.getLogger(__name__)
        self.constants = RegistrationAndSignInPageConstants

    def registration(self, user: UserData):
        """Register a new user with valid credentials"""
        self.wait_and_fill_input_field(locator_type=By.XPATH, locator=self.constants.INPUT_FIRST_NAME_XPATH, text=user.first_name)
        self.wait_and_fill_input_field(locator_type=By.XPATH, locator=self.constants.INPUT_LAST_NAME_XPATH, text=user.last_name)
        self.wait_and_fill_input_field(locator_type=By.XPATH, locator=self.constants.INPUT_EMAIL_XPATH, text=user.email)
        self.wait_and_fill_input_field(locator_type=By.XPATH, locator=self.constants.INPUT_PHONE_NUMBER_XPATH, text=user.phone_number)
        self.wait_and_fill_input_field(locator_type=By.XPATH, locator=self.constants.INPUT_PASSWORD_XPATH, text=user.password)
        self.log.info('Filed required fields on registration form')
        self.wait_and_click(locator_type=By.XPATH, locator=self.constants.FINISH_REGISTER_BUTTON_XPATH)
        self.log.info('Finish registration')

        from pages.start_page import StartPage
        return StartPage(self.driver)

    def sign_in(self, user: UserData):
        """Successful Sign In using valid credentials"""
        # Fill required fields and click "Sign In"
        self.wait_and_fill_input_field(locator_type=By.XPATH, locator=self.constants.SIGN_IN_EMAIL_INPUT_XPATH, text=user.email)
        self.wait_and_fill_input_field(locator_type=By.XPATH, locator=self.constants.SIGN_IN_PASSWORD_INPUT_XPATH, text=user.password)
        self.log.info('Filled required fields')
        self.wait_and_click(locator_type=By.XPATH, locator=self.constants.SUCCESS_SIGN_IN_BUTTON_XPATH)
        self.log.info('Successful Sign In')

        from pages.start_page import StartPage
        return StartPage(self.driver)
