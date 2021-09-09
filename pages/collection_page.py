import logging

from selenium.webdriver.common.by import By

from constants.collection_page_constants import CollectionPageConstants
from helpers.base_helpers import BaseHelpers


class CollectionPage(BaseHelpers):
    """Store of helpers related to Profile page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = CollectionPageConstants
        self.log = logging.getLogger(__name__)

    def go_to_favourite_item(self):
        """Go to favourite item page"""
        self.wait_and_click(locator_type=By.XPATH, locator=self.constants.FIRST_ITEM_IN_FAVOURITE_LIST_XPATH)

        from pages.product_page import ProductPage
        return ProductPage(self.driver)
