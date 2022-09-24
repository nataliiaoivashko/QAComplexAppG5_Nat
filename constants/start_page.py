class StartPageConstants:
    # SIGN IN
    SIGN_IN_USERNAME_FIELD_XPATH = ".//input[@placeholder='Username']"
    SIGN_IN_PASSWORD_FIELD_XPATH = ".//input[@placeholder='Password']"
    SIGN_IN_BUTTON_XPATH = ".//button[text()='Sign In']"

    SIGN_IN_LOGIN_ERROR_XPATH = ".//div[@class='alert alert-danger text-center']"
    SIGN_IN_LOGIN_ERROR_TEXT = "Invalid username / pasword"

    # SIGN UP
    SIGN_UP_USERNAME_FIELD_XPATH = ".//input[@id='username-register']"
    SIGN_UP_EMAIL_FIELD_XPATH = ".// input[ @ id = 'email-register']"
    SIGN_UP_PASSWORD_FIELD_XPATH = ".//input[@id='password-register']"
    SIGN_UP_BUTTON_XPATH = ".//button[text()='Sign up for OurApp']"

    SIGN_UP_LOGIN_ERROR_XPATH = ".//div[@class='alert alert-danger small liveValidateMessage " \
                                "liveValidateMessage--visible'] "
    SIGN_UP_EMAIL_ERROR_XPATH1 = ".//div[@class='alert alert-danger small liveValidateMessage " \
                                 "liveValidateMessage--visible']"  # regular error email xpath
    SIGN_UP_EMAIL_ERROR_XPATH = ".//div[@class='alert alert-danger small']"  # xpath that shows up rarely
    SIGN_UP_PASSWORD_ERROR_XPATH = ".//div[@class='alert alert-danger small liveValidateMessage " \
                                   "liveValidateMessage--visible'] "
    SIGN_UP_LOGIN_ERROR_TEXT_LENGTH = "Username must be at least 3 characters."
    SIGN_UP_LOGIN_ERROR_TEXT_LENGTH_TOO_LONG = "Username cannot exceed 30 characters."
    SIGN_UP_LOGIN_ERROR_TEXT_SPACES = "Username can only contain letters and numbers."
    SIGN_UP_EMAIL_ERROR_TEXT = "You must provide a valid email address."
    SIGN_UP_PASSWORD_ERROR_TEXT_LENGTH = "Password must be at least 12 characters."
    SIGN_UP_PASSWORD_ERROR_TEXT_LENGTH_TOO_LONG = "Password cannot exceed 50 characters."
