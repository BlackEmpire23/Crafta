class ProfilePageConstants:
    """Store constants related to Profile page"""

    # Main information
    FIRST_NAME_INPUT_FIELD_XPATH = './/input[@id="first_name"]'
    LAST_NAME_INPUT_FIELD_XPATH = './/input[@id="last_name"]'
    ABOUT_INPUT_FIELD_XPATH = './/textarea[@id="about"]'
    WEB_SITE_INPUT_FIELD_XPATH = './/input[@id="web_site"]'
    SAVE_BUTTON_XPATH = './/*[@id="main-settings"]/form/div[10]/button'
    SUCCESS_MESSAGE_TEXT = "Данные успешно изменены."
    SUCCESS_MESSAGE_XPATH = './html/body/div[2]/div[3]/div/div/div'
