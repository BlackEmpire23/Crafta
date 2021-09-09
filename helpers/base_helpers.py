import random
import string

import selenium.webdriver.support.expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from constants.base_constants import BaseConstants
from constants.text import TEXT_BASE_RUS


def create_driver(browser_name):
    """Create driver based on browser's name"""
    if browser_name == BaseConstants.CHROME:
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        return webdriver.Chrome(executable_path=BaseConstants.CHROME_DRIVER_PATH, options=options)
    if browser_name == BaseConstants.FIREFOX:
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        return webdriver.Firefox(executable_path=BaseConstants.FIREFOX_DRIVER_PATH, options=options)
    else:
        raise ValueError(f"Unknown browser name:{browser_name}")


def create_random_text(word_count=10):
    """Generate random text based on base text"""
    sample_text_lst = TEXT_BASE_RUS.replace('\n', '').split(' ')
    generate_text_lst = []
    for i in range(word_count):
        generate_text_lst.append(random.choice(sample_text_lst))
    generate_text = ' '.join(generate_text_lst)
    return generate_text


def create_random_email(symbols=7):
    """Generator of random email"""
    email = 'www.'
    for i in range(symbols):
        email += random.choice(random.choice(string.ascii_letters).lower())
    return email + '.com'


def random_name(symbols=6):
    """Generator of random name"""
    name = ''
    for i in range(symbols):
        name += random.choice(random.choice(string.ascii_letters))
    return name


class BaseHelpers:
    """Scope of base helpers"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=5)

    def wait_and_fill_input_field(self, locator_type, locator, text=''):
        """Wait until element clickable and fill input field"""
        field = self.wait.until(EC.visibility_of_element_located((locator_type, locator)))
        field.clear()
        field.send_keys(text)

    def wait_and_click(self, locator_type, locator):
        """Wait until element clickable and click"""
        self.wait.until(EC.element_to_be_clickable((locator_type, locator)))
        self.driver.find_element(by=locator_type, value=locator).click()

    def wait_until_element_find(self, locator_type, locator):
        """ Wait until element find and return it """
        self.wait.until(EC.presence_of_element_located((locator_type, locator)))
        return self.driver.find_element(by=locator_type, value=locator)

    def verify_message_by_text(self, xpath, text):
        """ Verification by text """
        assert self.wait_until_element_find(locator_type=By.XPATH, locator=xpath).text == text

    def verify_element_appears(self, xpath):
        """Verification by present of element"""
        assert self.wait_until_element_find(locator_type=By.XPATH, locator=xpath)

    def save_current_url(self):
        """Return URL"""
        url = self.driver.current_url
        return url


class UserData:

    def __init__(self, first_name='', last_name='', email='', phone_number='', password=''):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.password = password
