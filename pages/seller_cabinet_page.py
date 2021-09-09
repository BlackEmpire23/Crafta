import logging

from selenium.webdriver.common.by import By

from constants.seller_cabinet_constants import SellerCabinetConstants
from helpers.base_helpers import BaseHelpers


class SellersCabinet(BaseHelpers):
    """Store of helpers related to Seller's page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = SellerCabinetConstants
        self.log = logging.getLogger(__name__)

    def edit_store_settings(self, name, domain, about):
        """Editing store settings"""
        self.wait_and_click(locator_type=By.XPATH, locator=self.constants.STORE_SETTINGS_BUTTON_XPATH)
        self.wait_and_click(locator_type=By.XPATH, locator=self.constants.ACTIVATE_STORE_BUTTON_XPATH)
        self.wait_and_fill_input_field(locator_type=By.XPATH, locator=self.constants.BRAND_NAME_INPUT_XPATH, text=name)
        self.wait_and_fill_input_field(locator_type=By.XPATH, locator=self.constants.DOMAIN_NAME_INPUT_XPATH, text=domain)
        self.wait_and_fill_input_field(locator_type=By.XPATH, locator=self.constants.DESCRIPTION_TEXTAREA_FIELD_XPATH, text=about)
        self.log.info("Filled required fields")
        self.wait_and_click(locator_type=By.XPATH, locator=self.constants.SAVE_CHANGES_BUTTON_XPATH)
        self.log.info("Save changes")

    def verify_changes(self):
        """Verify changes by success message"""
        self.verify_message_by_text(xpath=self.constants.SUCCESS_MESSAGE_XPATH, text=self.constants.SUCCESS_MESSAGE_TEXT)
        self.log.info("Changes verified")
