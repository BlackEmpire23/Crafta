import os


class BaseConstants:
    """Store of base constants"""

    current_module = os.path.dirname(os.path.abspath(__file__))
    sep = os.path.sep
    CHROME_DRIVER_PATH = f'{current_module}{sep}..{sep}drivers{sep}chromedriver.exe'
    FIREFOX_DRIVER_PATH = f'{current_module}{sep}..{sep}drivers{sep}geckodriver.exe'
    START_PAGE_URL = "https://crafta.ua/"

    CHROME = 'chrome'
    FIREFOX = 'firefox'
