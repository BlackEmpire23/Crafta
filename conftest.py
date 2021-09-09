import logging
import random
import string

import pytest

from constants.base_constants import BaseConstants
from helpers.base_helpers import UserData
from pages.start_page import StartPage


class BaseTest:
    log = logging.getLogger(__name__)


@pytest.fixture(scope="function")
def start_page(driver):
    driver.get(BaseConstants.START_PAGE_URL)
    return StartPage(driver)


@pytest.fixture(scope="function")
def logout(driver):
    yield
    StartPage(driver).logout()


@pytest.fixture(scope="function")
def user():
    """ Valid data for user credentials """
    first_name_text = ''
    for i in range(random.randint(4, 6)):
        first_name_text += random.choice(string.ascii_letters)
    last_name_text = ''
    for i in range(random.randint(4, 6)):
        last_name_text += random.choice(string.ascii_letters)
    email_text = ''
    for i in range(random.randint(5, 20)):
        email_text += random.choice(string.ascii_letters).lower()
    email_text += '@gmail.com'
    phone_number = random.choice(['050', '099', '067', '098', '063', '093'])
    for i in range(7):
        phone_number += str(random.randint(0, 9))
    password_text = ''
    for i in range(random.randint(4, 13)):
        password_text += random.choice(string.ascii_letters)
        password_text += random.choice(string.punctuation)
        password_text += str(random.randint(1, 9))
    return UserData(first_name_text, last_name_text, email_text, phone_number, password_text)
