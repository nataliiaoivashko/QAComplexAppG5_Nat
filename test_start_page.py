import logging

import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.start_page import StartPage
from pages.utils import random_str, random_num


# import pages
# from time import sleep
# from selenium.webdriver.common.by import By


class TestStartPage:
    log = logging.getLogger("[StartPAge]")

    @pytest.fixture(scope="function")
    def start_page(self):
        driver = webdriver.Chrome(DRIVER_PATH)
        driver.get(BASE_URL)
        yield StartPage(driver)
        driver.close()

    def test_incorrect_login(self, start_page):
        """
        -Preconditions:
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
        # login as user
        start_page.sign_in("User11", "Psw11")
        self.log.info("Logged in as  non-existent user")

        # verify error
        start_page.verify_sign_in_error()
        self.log.info("error was verified")

    def test_empty_login(self, start_page):
        """
        -Preconditions:
            - Create driver
            - Open page
        - Steps:
            - EMPTY login
            - EMPTY password
            - Click button
            - Verify error
        - Post-conditions:
            - Close driver
        """
        # login as user
        start_page.sign_in("", "")
        self.log.info("Logged in as an empty user")

        # verify error
        start_page.verify_sign_in_error()
        self.log.info("empty user error was verified")

    def test_registration_login_check_successful(self, start_page):
        """
        - Preconditions: Create driver, Open page
        - Steps: Fill login, email & password fields, then click registration button
        - Verify success (verify that Hello message shows up on next page)
        """
        # Prepare data
        user = random_str()
        username_value = f"{user}{random_num()}"
        email_value = f"{user}{random_num()}@mail.com"
        password_value = f"{random_str(6)}{random_num()}"

        # Sign Up as the user
        start_page.sign_up(username_value, email_value, password_value)
        self.log.info("registered as a new user %s", username_value)

        # verify success message
        start_page.verify_sign_up_success(username_value)
        self.log.info("Hello message was verified")


"""===============below code still has to be refactored using new test framework:==================="""

# def test_registration_login_check_too_short():
#     """
#     - Create driver
#     - Open page
#     - Fill registration login (incorrectly)
#     - Fill registration email (correctly)
#     - Fill registration password (correctly)
#     - Verify error (verify that error message shows up)
#     """
#     # Create driver
#     driver = webdriver.Chrome("/Users/Nata/PycharmProjects/QAComplexAppG6/chromedriver.exe")
#     # C:\Users\Nata\PycharmProjects\QAComplexAppG6\chromedriver.exe
#
#     # Open page
#     driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
#
#     # fill registration login (incorrectly)
#     element = driver.find_element(by=By.XPATH, value=".//input[@id='username-register']")
#     print(element)
#     element.send_keys("Nt")
#     sleep(1)
#
#     # Fill registration email (correctly)
#     email = driver.find_element(by=By.XPATH, value=".//input[@id='email-register']")
#     print(email)
#     email.send_keys("you@example1.com")
#     sleep(1)
#
#     # Fill registration password (correctly)
#     password = driver.find_element(by=By.XPATH, value=".//input[@id='password-register']")
#     print(password)
#     password.send_keys("whatever_test55")
#     sleep(1)
#
#     # Verify error
#     error_element2 = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger small "
#                                                             "liveValidateMessage liveValidateMessage--visible']")
#     assert error_element2.text == "Username must be at least 3 characters.", f"Actual message:" \
#                                                                              f" {error_element2.text}"
#     sleep(1)
#
#     # Close driver
#     driver.close()
#
# def test_registration_login_check_too_long():
#     """
#     - Create driver
#     - Open page
#     - Fill registration login (incorrectly)
#     - Fill registration email (correctly)
#     - Fill registration password (correctly)
#     - Verify error (verify that error message shows up)
#     """
#     # Create driver
#     driver = webdriver.Chrome("/Users/Nata/PycharmProjects/QAComplexAppG6/chromedriver.exe")
#     # C:\Users\Nata\PycharmProjects\QAComplexAppG6\chromedriver.exe
#
#     # Open page
#     driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
#
#     # fill registration login (incorrectly)
#     element = driver.find_element(by=By.XPATH, value=".//input[@id='username-register']")
#     print(element)
#     element.send_keys("Login_that_is_longer_than_30_characters")
#     sleep(1)
#
#     # Fill registration email (correctly)
#     email = driver.find_element(by=By.XPATH, value=".//input[@id='email-register']")
#     print(email)
#     email.send_keys("you@example1.com")
#     sleep(1)
#
#     # Fill registration password (correctly)
#     password = driver.find_element(by=By.XPATH, value=".//input[@id='password-register']")
#     print(password)
#     password.send_keys("whatever_test_55")
#     sleep(1)
#
#     # Verify error
#     error_element2 = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger small "
#                                                             "liveValidateMessage liveValidateMessage--visible']")
#     assert error_element2.text == "Username cannot exceed 30 characters.", f"Actual message:" \
#                                                                            f" {error_element2.text}"
#     sleep(1)
#
#     # Close driver
#     driver.close()
#
# def test_registration_login_check_for_spaces():
#     """
#     - Create driver
#     - Open page
#     - Fill registration login (incorrectly)
#     - Fill registration email (correctly)
#     - Fill registration password (correctly)
#     - Verify error (verify that error message shows up)
#     """
#     # Create driver
#     driver = webdriver.Chrome("/Users/Nata/PycharmProjects/QAComplexAppG6/chromedriver.exe")
#     # C:\Users\Nata\PycharmProjects\QAComplexAppG6\chromedriver.exe
#
#     # Open page
#     driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
#
#     # fill registration login (incorrectly)
#     element = driver.find_element(by=By.XPATH, value=".//input[@id='username-register']")
#     print(element)
#     element.send_keys("contains1 space")
#     sleep(1)
#
#     # Fill registration email (correctly)
#     email = driver.find_element(by=By.XPATH, value=".//input[@id='email-register']")
#     email.send_keys("myself@example5.com")
#     sleep(1)
#
#     # Fill registration password (correctly)
#     password = driver.find_element(by=By.XPATH, value=".//input[@id='password-register']")
#     password.send_keys("whatever_test55")
#     sleep(1)
#
#     # Verify error
#     error_element2 = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger small "
#                                                             "liveValidateMessage liveValidateMessage--visible']")
#     assert error_element2.text == "Username can only contain letters and numbers.", f"Actual message:" \
#                                                                                     f" {error_element2.text}"
#     sleep(1)
#
#     # Close driver
#     driver.close()
#
# def test_registration_login_check_for_special_char():
#     """
#     - Create driver
#     - Open page
#     - Fill registration login (incorrectly)
#     - Fill registration email (correctly)
#     - Fill registration password (correctly)
#     - Verify error (verify that error message shows up)
#     """
#     # Create driver
#     driver = webdriver.Chrome("/Users/Nata/PycharmProjects/QAComplexAppG6/chromedriver.exe")
#     # C:\Users\Nata\PycharmProjects\QAComplexAppG6\chromedriver.exe
#
#     # Open page
#     driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
#
#     # fill registration login (incorrectly)
#     element = driver.find_element(by=By.XPATH, value=".//input[@id='username-register']")
#     print(element)
#     element.send_keys("special,./!#")
#     sleep(1)
#
#     # Fill registration email (correctly)
#     email = driver.find_element(by=By.XPATH, value=".//input[@id='email-register']")
#     email.send_keys("myself@example5.com")
#     sleep(1)
#
#     # Fill registration password (correctly)
#     password = driver.find_element(by=By.XPATH, value=".//input[@id='password-register']")
#     password.send_keys("whatever_test55")
#     sleep(1)
#
#     # Verify error
#     error_element2 = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger small "
#                                                             "liveValidateMessage liveValidateMessage--visible']")
#     assert error_element2.text == "Username can only contain letters and numbers.", f"Actual message:" \
#                                                                                     f" {error_element2.text}"
#
#     sleep(1)
#
#     # Close driver
#     driver.close()
#
# def test_registration_email_check1():
#     """
#     - Create driver
#     - Open page
#     - Fill registration login (correctly)
#     - Fill registration email (incorrectly)
#     - Fill registration password (correctly)
#     - click button "sign up for our app"
#     - Verify error (verify that error message shows up AFTER button-click)
#     """
#     # Create driver
#     driver = webdriver.Chrome("/Users/Nata/PycharmProjects/QAComplexAppG6/chromedriver.exe")
#     # C:\Users\Nata\PycharmProjects\QAComplexAppG6\chromedriver.exe
#
#     # Open page
#     driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
#
#     # fill registration login (correctly)
#     element = driver.find_element(by=By.XPATH, value=".//input[@id='username-register']")
#     element.send_keys("Nata")
#     sleep(1)
#
#     # Fill registration email (incorrectly)
#     email = driver.find_element(by=By.XPATH, value=".//input[@id='email-register']")
#     email.send_keys("myself@example")
#     sleep(1)
#
#     # Fill registration password (correctly)
#     password = driver.find_element(by=By.XPATH, value=".//input[@id='password-register']")
#     password.send_keys("whatever_test55")
#     sleep(1)
#
#     # Click button "SIGN UP FOR OUR APP"
#     button1 = driver.find_element(by=By.XPATH, value=".//button[text()='Sign up for OurApp']")
#     button1.click()
#     sleep(1)
#
#     # Verify error
#     error_element3 = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger small']")
#     assert error_element3.text == "You must provide a valid email address.", f"Actual message:" \
#                                                                              f" {error_element3.text}"
#
#     # Close driver
#     driver.close()
#
# def test_registration_email_check2():
#     """
#     - Create driver
#     - Open page
#     - Fill registration login (correctly)
#     - Fill registration email (incorrectly)
#     - Fill registration password (correctly)
#     - Verify error (verify that error message shows up BEFORE button-click)
#     """
#     # Create driver
#     driver = webdriver.Chrome("/Users/Nata/PycharmProjects/QAComplexAppG6/chromedriver.exe")
#     # C:\Users\Nata\PycharmProjects\QAComplexAppG6\chromedriver.exe
#
#     # Open page
#     driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
#
#     # fill registration login (correctly)
#     element = driver.find_element(by=By.XPATH, value=".//input[@id='username-register']")
#     element.send_keys("Nata")
#     sleep(1)
#
#     # Fill registration email (incorrectly)
#     email = driver.find_element(by=By.XPATH, value=".//input[@id='email-register']")
#     email.send_keys("myself_example1234qwerty")
#     sleep(1)
#
#     # Fill registration password (correctly)
#     password = driver.find_element(by=By.XPATH, value=".//input[@id='password-register']")
#     password.send_keys("whatever_test_16")
#     sleep(2)
#
#     # Verify error
#     error_element4 = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger small "
#                                                             "liveValidateMessage liveValidateMessage--visible']")
#     assert error_element4.text == "You must provide a valid email address.", f"Actual message:" \
#                                                                              f" {error_element4.text}"
#
#     # Close driver
#     driver.close()
#
# def test_registration_password_too_short():
#     """
#     - Create driver
#     - Open page
#     - Fill registration login (correctly)
#     - Fill registration email (correctly)
#     - Fill registration password (too short incorrectly)
#     - Verify error (verify that error message shows up)
#     """
#     # Create driver
#     driver = webdriver.Chrome("/Users/Nata/PycharmProjects/QAComplexAppG6/chromedriver.exe")
#     # C:\Users\Nata\PycharmProjects\QAComplexAppG6\chromedriver.exe
#
#     # Open page
#     driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
#
#     # fill registration login (do correctly)
#     element = driver.find_element(by=By.XPATH, value=".//input[@id='username-register']")
#     print(element)
#     element.send_keys("Nata")
#     sleep(1)
#
#     # Fill registration email (do correctly)
#     password = driver.find_element(by=By.XPATH, value=".//input[@id='email-register']")
#     password.send_keys("lifeguard85@gmail.com")
#     sleep(1)
#
#     # Fill registration password (do incorrectly: try less than 12 char)
#     password = driver.find_element(by=By.XPATH, value=".//input[@id='password-register']")
#     password.send_keys("less")
#     sleep(1)
#
#     # Verify error
#     error_element1 = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger small "
#                                                             "liveValidateMessage liveValidateMessage--visible']")
#     assert error_element1.text == "Password must be at least 12 characters.", f"Actual message:" \
#                                                                               f" {error_element1.text}"
#     sleep(1)
#
#     # Close driver
#     driver.close()
#
# def test_registration_password_too_long():
#     """
#     - Create driver
#     - Open page
#     - Fill registration login (correctly)
#     - Fill registration email (correctly)
#     - Fill registration password (incorrectly)
#     - Verify error (verify that error message shows up)
#     """
#     # Create driver
#     driver = webdriver.Chrome("/Users/Nata/PycharmProjects/QAComplexAppG6/chromedriver.exe")
#     # C:\Users\Nata\PycharmProjects\QAComplexAppG6\chromedriver.exe
#
#     # Open page
#     driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
#
#     # fill registration login (do correctly)
#     element = driver.find_element(by=By.XPATH, value=".//input[@id='username-register']")
#     print(element)
#     element.send_keys("Nata")
#     sleep(1)
#
#     # Fill registration email (do correctly)
#     password = driver.find_element(by=By.XPATH, value=".//input[@id='email-register']")
#     password.send_keys("test_email@examples.com")
#     sleep(1)
#
#     # Fill registration password (do incorrectly: try less than 12 char)
#     password = driver.find_element(by=By.XPATH, value=".//input[@id='password-register']")
#     password.send_keys("this_password_exceeds_50_characters_for_testing_purposes")
#     sleep(1)
#
#     # Verify error
#     error_element1 = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger small "
#                                                             "liveValidateMessage liveValidateMessage--visible']")
#     assert error_element1.text == "Password cannot exceed 50 characters.", f"Actual message:" \
#                                                                            f" {error_element1.text}"
#     sleep(1)
#
#     # Close driver
#     driver.close()
