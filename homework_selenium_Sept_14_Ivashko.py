from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRegistration:

    def test_registration_login(self):
        """
        - Create driver
        - Open page
        - Fill registration login
        - Fill registration password
        - Click button "SIGN UP FOR OUR APP"
        - Verify error
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
        sleep(2)

        # # Click button "SIGN UP FOR OUR APP"
        # button = driver.find_element(by=By.XPATH, value=".//button[@id='registration-form'']/button")
        # button.click()
        # sleep(1)

        # Verify error
        error_element = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        assert error_element.text == "Password must be at least 12 characters.", f"Actual message: {error_element.text}"

        # xpath for error:  // *[ @ id = "registration-form"] / div[3] / div ??

        # Close driver
        driver.close()
