import logging

from selenium.webdriver.common.by import By

from constants.catalog_page_constants import CatalogPageConstants
from helpers.base_helpers import BaseHelpers


class CatalogPage(BaseHelpers):
    """Store of helpers related to Profile page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = CatalogPageConstants
        self.log = logging.getLogger(__name__)

    def select_first_item_in_catalog(self):
        """Select the first item in catalog(not related to special stores)"""
        self.wait_and_click(locator_type=By.XPATH, locator=self.constants.FIRST_ITEM_IN_CATALOG_XPATH)
        self.log.info("Item selected")

        from pages.product_page import ProductPage
        return ProductPage(self.driver)
