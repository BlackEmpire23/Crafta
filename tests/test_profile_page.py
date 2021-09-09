import pytest

from conftest import BaseTest
from constants.base_constants import BaseConstants
from helpers.base_helpers import create_driver, random_name, create_random_email, create_random_text


@pytest.mark.parametrize("browser_name", [BaseConstants.CHROME, BaseConstants.FIREFOX])
class TestProfilePage(BaseTest):
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

    def test_edit_personal_data(self, start_page, register, logout):
        """
        Pre-conditions:
            1. Register a new user.
        STR:
            1. Go to "My Profile" page.
            2. Change fields: first name, last name, website, about yourself.
            3. Save changes.
            4. Verify result.
        Post-condition:
            1. Logout.
        """
        # 1. Go to "My Profile" page.
        profile_page = start_page.go_to_profile_page()

        # 2. Change fields: first name, last name, website, about yourself.
        # 3. Save changes.
        # 4. Verify result.
        first_name = random_name(symbols=7)
        last_name = random_name(symbols=5)
        website = create_random_email(symbols=6)
        about_text = create_random_text(word_count=15)
        profile_page.edit_personal_data(first_name=first_name, last_name=last_name, web_site=website, about_text=about_text)
