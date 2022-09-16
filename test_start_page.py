from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestStartPage:

    def test_incorrect_login(self):
        """
        - Create driver
        - Open page
        - Fill login
        - Fill password
        - Click button
        - Verify error
        """
        # Create driver
        driver = webdriver.Chrome("/Users/Nata/PycharmProjects/QAComplexAppG6/chromedriver.exe")
        # C:\Users\Nata\PycharmProjects\QAComplexAppG6\chromedriver.exe

        # Open page !!!
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        # fill login and or find elem
        element = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        print(element)
        element.send_keys("User11")
        sleep(1)

        # Fill password
        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        print(password)
        password.send_keys("Psw11")
        sleep(1)

        # Click button
        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        button.click()
        sleep(1)

        # Verify error
        error_element = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        assert error_element.text == "Invalid username / pasword", f"Actual message: {error_element.text}"

        # Close driver
        driver.close()

    def test_empty_login(self):
        """
            - Create driver
            - Open page
            - Clear login
            - Clear password
            - Click button
            - Verify error
            """
        # Create driver
        driver = webdriver.Chrome("/Users/Nata/PycharmProjects/QAComplexAppG6/chromedriver.exe")
        # C:\Users\Nata\PycharmProjects\QAComplexAppG6\chromedriver.exe

        # Open page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        # clear login
        element = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        print(element)
        element.clear()
        sleep(1)

        # Fill password
        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        print(password)
        password.clear()
        sleep(1)

        # Click button
        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        button.click()
        sleep(1)

        # Verify error
        error_element = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        assert error_element.is_displayed()
        assert error_element.text == "Invalid username / pasword", f"Actual message: {error_element.text}"

        # Close driver
        driver.close()

    def test_registration_login_check_too_short(self):
        """
        - Create driver
        - Open page
        - Fill registration login (incorrectly)
        - Fill registration email (correctly)
        - Fill registration password (correctly)
        - Verify error (verify that error message shows up)
        """
        # Create driver
        driver = webdriver.Chrome("/Users/Nata/PycharmProjects/QAComplexAppG6/chromedriver.exe")
        # C:\Users\Nata\PycharmProjects\QAComplexAppG6\chromedriver.exe

        # Open page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        # fill registration login (incorrectly)
        element = driver.find_element(by=By.XPATH, value=".//input[@id='username-register']")
        print(element)
        element.send_keys("Nt")
        sleep(1)

        # Fill registration email (correctly)
        email = driver.find_element(by=By.XPATH, value=".//input[@id='email-register']")
        print(email)
        email.send_keys("you@example1.com")
        sleep(1)

        # Fill registration password (correctly)
        password = driver.find_element(by=By.XPATH, value=".//input[@id='password-register']")
        print(password)
        password.send_keys("whatevertest55")
        sleep(1)

        # Verify error
        error_element2 = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger small "
                                                                "liveValidateMessage liveValidateMessage--visible']")
        assert error_element2.text == "Username must be at least 3 characters.", f"Actual message:" \
                                                                                 f" {error_element2.text}"
        sleep(1)

        # Close driver
        driver.close()

    def test_registration_login_check_too_long(self):
        """
        - Create driver
        - Open page
        - Fill registration login (incorrectly)
        - Fill registration email (correctly)
        - Fill registration password (correctly)
        - Verify error (verify that error message shows up)
        """
        # Create driver
        driver = webdriver.Chrome("/Users/Nata/PycharmProjects/QAComplexAppG6/chromedriver.exe")
        # C:\Users\Nata\PycharmProjects\QAComplexAppG6\chromedriver.exe

        # Open page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        # fill registration login (incorrectly)
        element = driver.find_element(by=By.XPATH, value=".//input[@id='username-register']")
        print(element)
        element.send_keys("Natashasloginistoolongmorethan30")
        sleep(1)

        # Fill registration email (correctly)
        email = driver.find_element(by=By.XPATH, value=".//input[@id='email-register']")
        email.send_keys("myself@example5.com")
        sleep(1)

        # Fill registration password (correctly)
        password = driver.find_element(by=By.XPATH, value=".//input[@id='password-register']")
        password.send_keys("whatevertest55")
        sleep(1)

        # Verify error
        error_element2 = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger small "
                                                                "liveValidateMessage liveValidateMessage--visible']")
        assert error_element2.text == "Username cannot exceed 30 characters.", f"Actual message:" \
                                                                               f" {error_element2.text}"
        sleep(1)

        # Close driver
        driver.close()

    def test_registration_login_check_for_spaces(self):
        """
        - Create driver
        - Open page
        - Fill registration login (incorrectly)
        - Fill registration email (correctly)
        - Fill registration password (correctly)
        - Verify error (verify that error message shows up)
        """
        # Create driver
        driver = webdriver.Chrome("/Users/Nata/PycharmProjects/QAComplexAppG6/chromedriver.exe")
        # C:\Users\Nata\PycharmProjects\QAComplexAppG6\chromedriver.exe

        # Open page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        # fill registration login (incorrectly)
        element = driver.find_element(by=By.XPATH, value=".//input[@id='username-register']")
        print(element)
        element.send_keys("contains1 space")
        sleep(1)

        # Fill registration email (correctly)
        email = driver.find_element(by=By.XPATH, value=".//input[@id='email-register']")
        email.send_keys("myself@example5.com")
        sleep(1)

        # Fill registration password (correctly)
        password = driver.find_element(by=By.XPATH, value=".//input[@id='password-register']")
        password.send_keys("whatevertest55")
        sleep(1)

        # Verify error
        error_element2 = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger small "
                                                                "liveValidateMessage liveValidateMessage--visible']")
        assert error_element2.text == "Username can only contain letters and numbers.", f"Actual message:" \
                                                                                        f" {error_element2.text}"
        sleep(1)

        # Close driver
        driver.close()

    def test_registration_login_check_for_special_char(self):
        """
        - Create driver
        - Open page
        - Fill registration login (incorrectly)
        - Fill registration email (correctly)
        - Fill registration password (correctly)
        - Verify error (verify that error message shows up)
        """
        # Create driver
        driver = webdriver.Chrome("/Users/Nata/PycharmProjects/QAComplexAppG6/chromedriver.exe")
        # C:\Users\Nata\PycharmProjects\QAComplexAppG6\chromedriver.exe

        # Open page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        # fill registration login (incorrectly)
        element = driver.find_element(by=By.XPATH, value=".//input[@id='username-register']")
        print(element)
        element.send_keys("special,./!#")
        sleep(1)

        # Fill registration email (correctly)
        email = driver.find_element(by=By.XPATH, value=".//input[@id='email-register']")
        email.send_keys("myself@example5.com")
        sleep(1)

        # Fill registration password (correctly)
        password = driver.find_element(by=By.XPATH, value=".//input[@id='password-register']")
        password.send_keys("whatevertest55")
        sleep(1)

        # Verify error
        error_element2 = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger small "
                                                                "liveValidateMessage liveValidateMessage--visible']")
        assert error_element2.text == "Username can only contain letters and numbers.", f"Actual message:" \
                                                                                        f" {error_element2.text}"

        sleep(1)

        # Close driver
        driver.close()

    def test_registration_email_check1(self):
        """
        - Create driver
        - Open page
        - Fill registration login (correctly)
        - Fill registration email (incorrectly)
        - Fill registration password (correctly)
        - click button "sign up for our app"
        - Verify error (verify that error message shows up AFTER button-click)
        """
        # Create driver
        driver = webdriver.Chrome("/Users/Nata/PycharmProjects/QAComplexAppG6/chromedriver.exe")
        # C:\Users\Nata\PycharmProjects\QAComplexAppG6\chromedriver.exe

        # Open page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        # fill registration login (correctly)
        element = driver.find_element(by=By.XPATH, value=".//input[@id='username-register']")
        element.send_keys("Nata")
        sleep(1)

        # Fill registration email (incorrectly)
        email = driver.find_element(by=By.XPATH, value=".//input[@id='email-register']")
        email.send_keys("myself@example")
        sleep(1)

        # Fill registration password (correctly)
        password = driver.find_element(by=By.XPATH, value=".//input[@id='password-register']")
        password.send_keys("whatevertest55")
        sleep(1)

        # Click button "SIGN UP FOR OUR APP"
        button1 = driver.find_element(by=By.XPATH, value=".//button[text()='Sign up for OurApp']")
        button1.click()
        sleep(1)

        # Verify error
        error_element3 = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger small']")
        assert error_element3.text == "You must provide a valid email address.", f"Actual message:" \
                                                                                 f" {error_element3.text}"

        # Close driver
        driver.close()

    def test_registration_email_check2(self):
        """
        - Create driver
        - Open page
        - Fill registration login (correctly)
        - Fill registration email (incorrectly)
        - Fill registration password (correctly)
        - Verify error (verify that error message shows up BEFORE button-click)
        """
        # Create driver
        driver = webdriver.Chrome("/Users/Nata/PycharmProjects/QAComplexAppG6/chromedriver.exe")
        # C:\Users\Nata\PycharmProjects\QAComplexAppG6\chromedriver.exe

        # Open page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        # fill registration login (correctly)
        element = driver.find_element(by=By.XPATH, value=".//input[@id='username-register']")
        element.send_keys("Nata")
        sleep(1)

        # Fill registration email (incorrectly)
        email = driver.find_element(by=By.XPATH, value=".//input[@id='email-register']")
        email.send_keys("myselfexample1234qwerty")
        sleep(1)

        # Fill registration password (correctly)
        password = driver.find_element(by=By.XPATH, value=".//input[@id='password-register']")
        password.send_keys("whatever_test_16")
        sleep(2)

        # Verify error
        error_element4 = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger small "
                                                                "liveValidateMessage liveValidateMessage--visible']")
        assert error_element4.text == "You must provide a valid email address.", f"Actual message:" \
                                                                                 f" {error_element4.text}"

        # Close driver
        driver.close()

    def test_registration_password_too_short(self):
        """
        - Create driver
        - Open page
        - Fill registration login (correctly)
        - Fill registration email (correctly)
        - Fill registration password (too short incorrectly)
        - Verify error (verify that error message shows up)
        """
        # Create driver
        driver = webdriver.Chrome("/Users/Nata/PycharmProjects/QAComplexAppG6/chromedriver.exe")
        # C:\Users\Nata\PycharmProjects\QAComplexAppG6\chromedriver.exe

        # Open page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        # fill registration login (do correctly)
        element = driver.find_element(by=By.XPATH, value=".//input[@id='username-register']")
        print(element)
        element.send_keys("Nata")
        sleep(1)

        # Fill registration email (do correctly)
        password = driver.find_element(by=By.XPATH, value=".//input[@id='email-register']")
        password.send_keys("lifeguard85@gmail.com")
        sleep(1)

        # Fill registration password (do incorrectly: try less than 12 char)
        password = driver.find_element(by=By.XPATH, value=".//input[@id='password-register']")
        password.send_keys("less")
        sleep(1)

        # Verify error
        error_element1 = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger small "
                                                                "liveValidateMessage liveValidateMessage--visible']")
        assert error_element1.text == "Password must be at least 12 characters.", f"Actual message:" \
                                                                                  f" {error_element1.text}"
        sleep(1)

        # Close driver
        driver.close()

    def test_registration_password_too_long(self):
        """
        - Create driver
        - Open page
        - Fill registration login (correctly)
        - Fill registration email (correctly)
        - Fill registration password (incorrectly)
        - Verify error (verify that error message shows up)
        """
        # Create driver
        driver = webdriver.Chrome("/Users/Nata/PycharmProjects/QAComplexAppG6/chromedriver.exe")
        # C:\Users\Nata\PycharmProjects\QAComplexAppG6\chromedriver.exe

        # Open page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        # fill registration login (do correctly)
        element = driver.find_element(by=By.XPATH, value=".//input[@id='username-register']")
        print(element)
        element.send_keys("Nata")
        sleep(1)

        # Fill registration email (do correctly)
        password = driver.find_element(by=By.XPATH, value=".//input[@id='email-register']")
        password.send_keys("test_email@examples.com")
        sleep(1)

        # Fill registration password (do incorrectly: try less than 12 char)
        password = driver.find_element(by=By.XPATH, value=".//input[@id='password-register']")
        password.send_keys("this_password_exceeds_50_characters_for_testing_purposes")
        sleep(1)

        # Verify error
        error_element1 = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger small "
                                                                "liveValidateMessage liveValidateMessage--visible']")
        assert error_element1.text == "Password cannot exceed 50 characters.", f"Actual message:" \
                                                                               f" {error_element1.text}"
        sleep(1)

        # Close driver
        driver.close()
