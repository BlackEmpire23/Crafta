import pytest

from conftest import BaseTest
from constants.base_constants import BaseConstants
from helpers.base_helpers import create_driver


@pytest.mark.parametrize("browser_name", [BaseConstants.CHROME, BaseConstants.FIREFOX])
class TestRegistrationAndSignInPage(BaseTest):
    """Scope of tests related to start page"""

    @pytest.fixture(scope="function")
    def driver(self, browser_name):
        driver = create_driver(browser_name)
        yield driver
        driver.close()

    @pytest.fixture(scope="function")
    def register_and_logout(self, start_page, user):
        registration_and_sign_in_page = start_page.go_to_registration_page()
        start_page = registration_and_sign_in_page.registration(user)
        start_page.logout()

        return user

    def test_successful_registration(self, start_page, user, logout):
        """
        STR:
            1. Go to start page (https://crafta.ua/)
            2. Click on "Регистрация" button.
            3. Fill required fields with correct data and press "Зарегистрироваться" button.
            5. Verify result.
        Post-condition:
            1. Logout.
        """
        # Go to registration page
        registration_and_sign_in_page = start_page.go_to_registration_page()

        # Finish registration flow
        start_page = registration_and_sign_in_page.registration(user)

        # Verify result
        start_page.verify_success_register_or_sign_in()

    def test_success_sign_in(self, start_page, register_and_logout, logout):
        """
        Pre-conditions:
            1. Register a new user on https://crafta.ua/
            2. Logout.
        STR:
            1. Press "Вход" button.
            2. Fill required fields with correct data (which were using during registration).
            3. Verify result.
        Post-condition:
            1. Logout.
        """
        # Go to Sign In page
        registration_and_sign_in_page = start_page.go_to_sign_in_page()

        # Successful Sign In and verify result.
        start_page = registration_and_sign_in_page.sign_in(register_and_logout)
        start_page.verify_success_register_or_sign_in()
