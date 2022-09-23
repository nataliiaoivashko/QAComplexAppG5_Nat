import logging

import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.start_page import StartPage
from pages.utils import random_str, random_num, random_num_len


class TestStartPage:
    log = logging.getLogger("[StartPage]")

    @pytest.fixture(scope="function")
    def start_page(self):
        # Pre-conditions
        driver = webdriver.Chrome(DRIVER_PATH)
        driver.get(BASE_URL)
        driver.implicitly_wait(1)
        # Steps
        yield StartPage(driver)
        # Post-conditions
        driver.close()

    def test_incorrect_login(self, start_page):
        """
        - Pre-conditions:
            - Create driver
            - Open page
        - Steps:
            - Fill login
            - Fill password
            - Click button
            - Verify error
        - Post-conditions:
            - Close driver
        """
        # Login as a user
        start_page.sign_in("User11", "Psw11")
        self.log.info("Logged in as non-existing user")

        # Verify error
        start_page.verify_sign_in_error()
        self.log.info("Error was verified")

    def test_empty_login(self, start_page):
        """
        - Create driver
        - Open page
        - Clear empty login
        - Clear empty password
        - Click button
        - Verify error
        """
        # Login as a user
        start_page.sign_in("", "")
        self.log.info("Logged in as non-existing user")

        # Verify error
        start_page.verify_sign_in_error()
        self.log.info("Error was verified")

    def test_register(self, start_page):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill email, login and password fields
            - Click on Sign Up button
            - Verify registration is successful
        """
        # Prepare data
        user = random_str()
        username_value = f"{user}{random_num()}"
        email_value = f"{user}{random_num()}@mail.com"
        password_value = f"{random_str(6)}{random_num()}"

        # Sign Up as a user
        hello_page = start_page.sign_up_and_verify(username_value, email_value, password_value)
        self.log.info("Signed Up as user %s", username_value)

        # Verify success message
        hello_page.verify_success_sign_up(username_value)
        self.log.info("Hello message was verified")

    # ===============my own code that was refactored using new test framework:==================

    def test_register_login_too_short(self, start_page):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill fields: email(as expected), login(incorrectly: too short) and password (as expected)
            - Click on Sign Up button
            - Verify error
        """
        # Prepare data
        user = random_str(length=1)
        username_value = f"{user}{random_num_len()}"
        email_value = f"{user}{random_num()}@mail.com"
        password_value = f"{random_str(6)}{random_num()}"

        # Sign Up as a user
        start_page.sign_up(username_value, email_value, password_value)
        self.log.info("Signed Up as user %s", username_value)

        # Verify error message
        start_page.verify_sign_up_error()
        self.log.info("Error was verified")

    def test_registration_login_check_too_long(self, start_page):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill registration login (incorrectly: more than 30 characters)
            - Fill registration email (correctly)
            - Fill registration password (correctly)
            - Verify error (verify that error message shows up)
        """
        # Prepare data
        user = random_str(length=31)
        username_value = f"{user}{random_num()}"
        email_value = f"{user}{random_num()}@mail.com"
        password_value = f"{random_str(6)}{random_num()}"

        # Sign Up as a user
        start_page.sign_up(username_value, email_value, password_value)
        self.log.info("Signed Up as user %s", username_value)

        # Verify error message
        start_page.verify_sign_up_error2()
        self.log.info("Error was verified")

    def test_registration_login_check_for_spaces(self, start_page):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill registration login (incorrectly: insert space)
            - Fill registration email (correctly)
            - Fill registration password (correctly)
            - Verify error (verify that error message shows up)
        """
        # Prepare data
        user = random_str()
        username_value = f"{user} {random_num()}"
        email_value = f"{user}{random_num()}@mail.com"
        password_value = f"{random_str(6)}{random_num()}"

        # Sign Up as a user
        start_page.sign_up(username_value, email_value, password_value)
        self.log.info("Signed Up as user %s", username_value)

        # Verify error message
        start_page.verify_sign_up_error3()
        self.log.info("Error was verified")

    def test_registration_login_check_for_special_char(self, start_page):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill registration login (incorrectly: special chars)
            - Fill registration email (correctly)
            - Fill registration password (correctly)
            - Verify error (verify that error message shows up)
        """
        # Prepare data
        user = random_str()
        username_value = f"{user},./!#{random_num()}"
        email_value = f"{user}{random_num()}@mail.com"
        password_value = f"{random_str(6)}{random_num()}"

        # Sign Up as a user
        start_page.sign_up(username_value, email_value, password_value)
        self.log.info("Signed Up as user %s", username_value)

        # Verify error message
        start_page.verify_sign_up_error3()
        self.log.info("Error was verified.")

    # def test_registration_email_check(self, start_page):
    #     """
    #     - Pre-conditions: Open start page
    #     - Steps:
    #         - Fill registration login and password (correctly)
    #         - Fill registration email (incorrectly "myself@example")
    #         - Click button "Sign Up For Our App" & verify that error message shows up AFTER button-click)
    #     """
    #     # Prepare data
    #     user = random_str()
    #     username_value = f"{user}{random_num()}"
    #     email_value = f"{user}{random_num()}@mail"
    #     password_value = f"{random_str(6)}{random_num()}"
    #
    #     # Sign Up as a user
    #     start_page.sign_up(username_value, email_value, password_value)
    #     self.log.info("Signed Up as user %s", username_value)
    #
    #     # Verify error message
    #     start_page.verify_sign_up_error_email_format()
    #     self.log.info("Error was verified.")

    def test_registration_email_check2(self, start_page):
        """
        - Open page
        - Fill registration login (correctly)
        - Fill registration email (incorrectly)
        - Fill registration password (correctly)
        - Verify error (verify that error message shows up BEFORE button-click)
        """
        # Prepare data
        user = random_str()
        username_value = f"{user}{random_num()}"
        email_value = f"{user}{random_num()}random"
        password_value = f"{random_str(6)}{random_num()}"

        # Sign Up as a user
        start_page.sign_up(username_value, email_value, password_value)
        self.log.info("Signed Up as user %s", username_value)

        # Verify error message
        start_page.verify_sign_up_error_email_format()
        self.log.info("Error was verified. Wrong email format")

    def test_registration_password_too_short(self, start_page):
        """
        Steps:
        - Open page
        - Fill registration login (correctly)
        - Fill registration email (correctly)
        - Fill registration password (too short incorrectly)
        - Verify error (verify that error message shows up)
        """
        # Prepare data
        user = random_str()
        username_value = f"{user}{random_num()}"
        email_value = f"{user}{random_num()}@mail.com"
        password_value = f"{random_str(3)}{random_num_len()}"

        # Sign Up as a user
        start_page.sign_up(username_value, email_value, password_value)
        self.log.info("Signed Up as user %s", username_value)

        # Verify error message
        start_page.verify_sign_up_error_password_length()
        self.log.info("Error was verified. password is too short ")

    def test_registration_password_too_long(self, start_page):
        """
        - Create driver,Open page
        - Fill registration login and email (correctly)
        - Fill registration password (incorrectly: more than 50 chars passwords)
        - Verify error (verify that error message shows up)
        """
        # Prepare data
        user = random_str()
        username_value = f"{user}{random_num()}"
        email_value = f"{user}{random_num()}@mail.com"
        password_value = f"{random_str(51)}{random_num_len(11, 99)}"

        # Sign Up as a user
        start_page.sign_up(username_value, email_value, password_value)
        self.log.info("Signed Up as user %s", username_value)

        # Verify error message
        start_page.verify_sign_up_error_password_length2()
        self.log.info("Error was verified. password is too long.")

    # self.log.info(str(password_value))
    # TODO: WHAT ID THERE ARE MULTIPLE ERRORS? HOW TO ASSERT 2-3 ERROR MESSAGES AT THE SAME TIME?
