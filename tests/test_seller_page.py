import pytest

from conftest import BaseTest
from constants.base_constants import BaseConstants
from helpers.base_helpers import create_driver, random_name


@pytest.mark.parametrize("browser_name", [BaseConstants.CHROME, BaseConstants.FIREFOX])
class TestSellerCabinetPage(BaseTest):
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

    def test_editing_store_info(self, start_page, register, logout):
        """
        Pre-conditions:
            1. Register a new user.
        STR:
            1. Go to sellers page.
            2. Go to edit store info page.
            3. Filled required fields and save.
            4. Verify changes.
        Post-condition:
            1. Logout.
        """
        # 1. Go to sellers page.
        seller_cabinet_page = start_page.go_to_sellers_cabinet()

        # 2. Go to edit store info page.
        # 3. Filled required fields and save.
        name = random_name()
        domain = random_name().lower()
        about = random_name(symbols=100)
        seller_cabinet_page.edit_store_settings(name=name, domain=domain, about=about)

        # 4. Verify changes.
        seller_cabinet_page.verify_changes()
