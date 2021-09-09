class RegistrationAndSignInPageConstants:
    """Store of constants related to Registration Sign In page"""

    # Registration form
    INPUT_FIRST_NAME_XPATH = './/input[@name="first_name"]'
    INPUT_LAST_NAME_XPATH = './/input[@name="last_name"]'
    INPUT_PHONE_NUMBER_XPATH = './/input[@name="phone"]'
    INPUT_EMAIL_XPATH = './/input[@name="email"]'
    INPUT_PASSWORD_XPATH = './/input[@name="password"]'
    FINISH_REGISTER_BUTTON_XPATH = './/button[@id="reg_btn"]'

    # Sign In form
    SIGN_IN_EMAIL_INPUT_XPATH = './/input[@name="username"]'
    SIGN_IN_PASSWORD_INPUT_XPATH = './/input[@name="password"]'
    SUCCESS_SIGN_IN_BUTTON_XPATH = './/button[@type="submit"]'
