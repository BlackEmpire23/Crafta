import pytest

from conftest import BaseTest
from constants.base_constants import BaseConstants
from helpers.base_helpers import create_driver


@pytest.mark.parametrize("browser_name", [BaseConstants.CHROME, BaseConstants.FIREFOX])
class TestCollection(BaseTest):
    """Store of tests related to Profile page"""

    @pytest.fixture(scope="function")
    def driver(self, browser_name):
        driver = create_driver(browser_name)
        yield driver
        driver.close()

    @pytest.fixture(scope="function")
    def register(self, start_page, user):
        registration_and_sign_in_page = start_page.go_to_registration_page()
        registration_and_sign_in_page.registration(user)

        return user

    def test_add_item_to_favourite(self, start_page, register, logout):
        """"""
        catalog_page = start_page.go_to_catalog_page()
        product_page = catalog_page.select_first_item_in_catalog()
        favourite_item = product_page.add_item_to_favourite(list_name="Избранное")
        collection_page = product_page.go_to_collection_page()
        collection_page.go_to_favourite_item()
        product_page.verify_favourite_item(favourite_item=favourite_item)
