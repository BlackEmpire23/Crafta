import logging

from selenium.webdriver.common.by import By

from constants.product_page import ProductPageConstants
from constants.start_page_constants import StartPageConstants
from helpers.base_helpers import BaseHelpers


class ProductPage(BaseHelpers):
    """Store of helpers related to Profile page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = ProductPageConstants
        self.log = logging.getLogger(__name__)

    def add_item_to_favourite(self, list_name):
        """Adding item to favourite"""
        self.wait_and_click(locator_type=By.XPATH, locator=self.constants.FAVOURITE_BUTTON_XPATH)
        self.wait_and_click(locator_type=By.XPATH, locator=self.constants.FAVOURITE_LIST_XPATH.format(list_name=list_name))
        item = self.save_current_url()
        self.log.info("Item added to favourite")

        return item

    def go_to_collection_page(self):
        """Go to collection page"""
        self.wait_and_click(locator_type=By.XPATH, locator=StartPageConstants.COLLECTION_BUTTON_XPATH)

        from pages.collection_page import CollectionPage
        return CollectionPage(self.driver)

    def verify_favourite_item(self, favourite_item):
        item = self.save_current_url()
        assert item == favourite_item
