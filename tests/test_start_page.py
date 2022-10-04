import logging

import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.start_page import StartPage
from pages.utils import User


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

    def test_incorrect_login(self, start_page, random_user):  # TEST 1: passed 02/10/2022
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
        start_page.sign_in(random_user)  # added ""random_user parameter""
        self.log.info("Logged in as non-existing user")

        # Verify error
        start_page.verify_sign_in_error()
        self.log.info("Error was verified")

    def test_empty_login(self, start_page):  # TEST 2: passed 02/10/2022
        """
        - Create driver
        - Open page
        - Clear empty login
        - Clear empty password
        - Click button
        - Verify error
        """
        # Login as a user
        start_page.sign_in(User())  # added fixture "User"
        self.log.info("Logged in as non-existing user")

        # Verify error
        start_page.verify_sign_in_error()
        self.log.info("Error was verified")

    def test_register(self, start_page, random_user):  # TEST 3: passed 02/10/2022
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill email, login and password fields
            - Click on Sign Up button
            - Verify registration is successful
        """

        # Sign Up as a user
        hello_page = start_page.sign_up_and_verify(random_user)  # added ""random_user parameter""
        self.log.info("Signed Up as user %s", random_user.username)

        # Verify success message
        hello_page.verify_success_sign_up(random_user.username)
        self.log.info("Hello message was verified")

    # ===============my own code that was refactored using new test framework:==================

    def test_register_login_too_short(self, start_page, random_user1):  # TEST 4: passed 02/10/2022
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill fields: email(as expected), login(incorrectly: too short) and password (as expected)
            - Click on Sign Up button
            - Verify error
        """

        # Sign Up as a user
        start_page.sign_up(random_user1)  # added "random_user1" to utils and conftest
        self.log.info("Signed Up as user %s", random_user1.username)

        # Verify error message
        start_page.verify_sign_up_error()
        self.log.info("Error was verified")

    def test_register_login_too_long(self, start_page, random_user2):  # TEST 5: passed 02/10/2022
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill registration login (incorrectly: more than 30 characters)
            - Fill registration email (correctly)
            - Fill registration password (correctly)
            - Verify error (verify that error message shows up)
        """

        # Sign Up as a user
        start_page.sign_up(random_user2)  # added "random_user2" to utils and conftest
        self.log.info("Signed Up as user %s", random_user2.username)

        # Verify error message
        start_page.verify_sign_up_error2()
        self.log.info("Error was verified")

    def test_register_login_spaces(self, start_page, random_user3):  # TEST 6: passed 02/10/2022
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill registration login (incorrectly: insert space)
            - Fill registration email (correctly)
            - Fill registration password (correctly)
            - Verify error (verify that error message shows up)
        """

        # Sign Up as a user
        start_page.sign_up(random_user3)  # added "random_user3" to utils and conftest
        self.log.info("Signed Up as user %s", random_user3.username)

        # Verify error message
        start_page.verify_sign_up_error3()
        self.log.info("Error was verified")

    def test_register_login_spec_char(self, start_page, random_user4):  # TEST 7: passed 02/10/2022
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill registration login (incorrectly: special chars)
            - Fill registration email (correctly)
            - Fill registration password (correctly)
            - Verify error (verify that error message shows up)
        """

        # Sign Up as a user
        start_page.sign_up(random_user4)  # added "random_user4" to utils & conftest
        self.log.info("Signed Up as user %s", random_user4.username)

        # Verify error message
        start_page.verify_sign_up_error3()
        self.log.info("Error was verified.")

    def test_register_password_too_short(self, start_page, random_user5):  # TEST 8: passed 02/10/2022
        """
        Steps:
        - Open page
        - Fill registration login (correctly)
        - Fill registration email (correctly)
        - Fill registration password (too short incorrectly)
        - Verify error (verify that error message shows up)
        """

        # Sign Up as a user
        start_page.sign_up(random_user5)  # added "random_user5" to utils & conftest
        self.log.info("Signed Up as user %s", random_user5.username)

        # Verify error message
        start_page.verify_sign_up_error_password_length()
        self.log.info("Error was verified. password is too short ")

    def test_register_password_too_long(self, start_page, random_user6):  # TEST 9: passed 02/10/2022
        """
        - Create driver,Open page
        - Fill registration login and email (correctly)
        - Fill registration password (incorrectly: more than 50 chars passwords)
        - Verify error (verify that error message shows up)
        """

        # Sign Up as a user
        start_page.sign_up(random_user6)  # added "random_user6" to utils & conftest
        self.log.info("Signed Up as user %s", random_user6.username)

        # Verify error message
        start_page.verify_sign_up_error_password_length2()
        self.log.info("Error was verified. password is too long.")

    def test_register_invalid_email_1(self, start_page, random_user7):  # TEST 10: passed 02/10/2022
        """
        - Open page
        - Fill registration login & password (correctly)
        - Fill registration email (incorrectly)
        - Click "Sign Up"
        - Verify error (verify that red error message shows up)
        """

        # Sign Up as a user
        start_page.sign_up(random_user7)  # added "random_user7" to utils & conftest
        self.log.info("Signed Up as user %s", random_user7.username)

        # Verify error message
        start_page.verify_sign_up_error_email_format()
        self.log.info("Error was verified. Wrong email format")

    def test_register_invalid_email_2(self, start_page, random_user8):  # TEST 11: passed 02/10/2022
        """
        - Open page
        - Fill registration login & password (correctly)
        - Fill registration email (incorrectly)
        - Click "Sign Up"
        - Verify error (verify that red error message shows up)
        """

        # Sign Up as a user
        start_page.sign_up(random_user8)  # added "random_user8" to utils & conftest
        self.log.info("Signed Up as user %s", random_user8.username)

        # Verify error message
        start_page.verify_sign_up_error_email_format()
        self.log.info("Error was verified. Wrong email format")

    # def test_register_invalid_email_3(self, start_page, random_user9):            # TEST 12: 2-Oct-2022: FAILS
    #     """
    #     - Open page
    #     - Fill registration login & password (correctly)
    #     - Fill registration email (incorrectly)
    #     - Click "Sign Up"
    #     - Verify error (verify that red error message shows up)"""
    #
    #     # Sign Up as a user
    #     start_page.sign_up(random_user9)                              # added "random_user9" to utils & conftest
    #     self.log.info("Signed Up as user %s", random_user9.username)
    #
    #     # Verify error message
    #     start_page.verify_sign_up_error_invalid_email_3()
    #     self.log.info("Error was verified. Incorrect email format")
