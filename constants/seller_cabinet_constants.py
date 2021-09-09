class SellerCabinetConstants:
    """Store of constants related to seller's cabinet"""

    # Store info
    STORE_SETTINGS_BUTTON_XPATH = './/*[@href="https://crafta.ua/my/settings/store"]'
    ACTIVATE_STORE_BUTTON_XPATH = './/span[@class="cft-switch__caption"]'
    BRAND_NAME_INPUT_XPATH = './/input[@id="title"]'
    DOMAIN_NAME_INPUT_XPATH = './/input[@id="subdomain_name"]'
    DESCRIPTION_TEXTAREA_FIELD_XPATH = './/textarea[@id="description"]'
    SAVE_CHANGES_BUTTON_XPATH = './/html/body/div[2]/div[3]/div/div/div/div[2]/div/form/div[8]/button'
    SUCCESS_MESSAGE_TEXT = "Данные успешно изменены."
    SUCCESS_MESSAGE_XPATH = './/html/body/div[2]/div[3]/div/div/div'
