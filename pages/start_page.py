import logging

from selenium.webdriver.common.by import By

from constants.start_page_constants import StartPageConstants
from helpers.base_helpers import BaseHelpers
from pages.profile_page import ProfilePage
from pages.registration_and_sign_in_page import RegistrationAndSignInPage


class StartPage(BaseHelpers):
    """Store of helpers related to Login page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.log = logging.getLogger(__name__)
        self.constants = StartPageConstants

    def go_to_registration_page(self):
        """Go to Registration page"""
        self.wait_and_click(locator_type=By.XPATH, locator=self.constants.REGISTRATION_BUTTON_XPATH)
        self.log.info('Go to registration page')

        return RegistrationAndSignInPage(self.driver)

    def verify_success_register_or_sign_in(self):
        """Verify success registration or Sign In"""
        self.wait_until_element_find(locator_type=By.XPATH, locator=self.constants.MY_PROFILE_ARROW_XPATH)
        self.verify_element_appears(xpath=self.constants.LOGOUT_BUTTON_XPATH)
        self.log.info("User logged in success")

    def logout(self):
        """Click on 'Log Out' button"""
        self.wait_and_click(locator_type=By.XPATH, locator=self.constants.MY_PROFILE_ARROW_XPATH)
        self.wait_and_click(locator_type=By.XPATH, locator=self.constants.LOGOUT_BUTTON_XPATH)
        self.log.info('Logged out')

        return StartPage(self.driver)

    def go_to_sign_in_page(self):
        """Go to Sign In page """
        # Click on "Sign In" button
        self.wait_and_click(locator_type=By.XPATH, locator=self.constants.SIGN_IN_BUTTON_XPATH)
        self.log.info('Go to Sign In form')

        return RegistrationAndSignInPage(self.driver)

    def go_to_profile_page(self):
        """Go to "My Profile" page"""
        self.wait_and_click(locator_type=By.XPATH, locator=self.constants.MY_PROFILE_ARROW_XPATH)
        self.wait_and_click(locator_type=By.XPATH, locator=self.constants.MY_SETTINGS_BUTTON_XPATH)

        return ProfilePage(self.driver)

    def go_to_catalog_page(self):
        """Click on "Catalog" button"""
        self.wait_and_click(locator_type=By.XPATH, locator=self.constants.CATALOG_BUTTON_XPATH)

        from pages.catalog_page import CatalogPage
        return CatalogPage(self.driver)

    def go_to_sellers_cabinet(self):
        """Go to @Seller's" cabinet"""
        self.wait_and_click(locator_type=By.XPATH, locator=self.constants.MY_PROFILE_ARROW_XPATH)
        self.wait_and_click(locator_type=By.XPATH, locator=self.constants.SELLER_CABINET_XPATH)
        self.log.info("Go to seller's cabinet")

        from pages.seller_cabinet_page import SellersCabinet
        return SellersCabinet(self.driver)
