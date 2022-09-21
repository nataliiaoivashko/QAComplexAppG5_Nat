import selenium
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def is_exists(self, xpath, by=By.XPATH):
        """Check that element exists"""
        try:
            self.driver.find_element(by=by, value=xpath)
            return True
        except selenium.common.exceptions.NoSuchElementException:
            return False

    def fill_field(self, xpath, value):
        """clear, fill field"""
        element = self.driver.find_element(by=By.XPATH, value=xpath)
        element.clear()
        element.send_keys(value)

    def click(self, xpath):
        """find and click"""
        button = self.driver.find_element(by=By.XPATH, value=xpath)
        button.click()

    def get_element_text(self, xpath):
        """find element and get text"""
        element = self.driver.find_element(by=By.XPATH, value=xpath)
        return element.text
