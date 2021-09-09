class StartPageConstants:
    """Store constants related to Start page"""

    # Header buttons
    REGISTRATION_BUTTON_XPATH = './/a[@href="https://crafta.ua/auth/register"]'
    MY_PROFILE_ARROW_XPATH = './/*[@class="style__root--2x4hI style__downIcon--1sBVO"]'
    LOGOUT_BUTTON_XPATH = './/a[@href="https://crafta.ua/auth/logout"]'
    SIGN_IN_BUTTON_XPATH = './/a[@href="https://crafta.ua/auth/login"]'
    MY_SETTINGS_BUTTON_XPATH = './/a[@href="https://crafta.ua/my/settings"]'
    SELLER_CABINET_XPATH = './/a[@href="https://crafta.ua/my/cabinet/orders/seller"]'

    # Catalog
    CATALOG_TEXT = "Каталог"
    CATALOG_BUTTON_XPATH = f'.//a[@href="https://crafta.ua/catalog/" and contains(text(),{CATALOG_TEXT})]'

    # Collection
    COLLECTION_BUTTON_XPATH = './/a[@href="https://crafta.ua/my/collections/"]'
