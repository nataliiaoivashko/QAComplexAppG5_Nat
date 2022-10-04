from constants.create_post_page import CreatePostPageConsts
from pages.base_page import BasePage
from pages.utils import log_decorator


class CreatePostPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = CreatePostPageConsts()
        from pages.header import Header
        self.header = Header(self.driver)

    @log_decorator
    def create_post(self, post):
        """Create post using provided values"""
        self.fill_field(xpath=self.constants.TITLE_FIELD_XPATH, value=post.title)
        self.fill_field(xpath=self.constants.BODY_FIELD_XPATH, value=post.body)
        self.click(xpath=self.constants.CREATE_POST_BUTTON_XPATH)

    @log_decorator
    def verify_successfully_created(self):
        """Verify success message"""
        assert self.get_element_text(xpath=self.constants.SUCCESS_MESSAGE_XPATH) == self.constants.SUCCESS_MESSAGE_TEXT, \
            f"Actual: {self.get_element_text(xpath=self.constants.SUCCESS_MESSAGE_XPATH)}"

    def create_post_with_checkbox(self, post):
        """Create post using provided values"""
        self.fill_field(xpath=self.constants.TITLE_FIELD_XPATH, value=post.title)
        self.fill_field(xpath=self.constants.BODY_FIELD_XPATH, value=post.body)

        self.click(xpath=self.constants.CHECKBOX_INPUT_XPATH)  # added checkbox click
        self.click(xpath=self.constants.DROPDOWN_LIST_XPATH)  # added dropdown click and one option select
        self.click(self.constants.VISIBILITY_SELECTION_XPATH.format(option=self.constants.OPTION_ONE_PERSON))
        self.click(xpath=self.constants.CREATE_POST_BUTTON_XPATH)

    @log_decorator
    def verify_checkbox(self):
        """Verify checkbox Unique"""

        assert self.get_element_text(self.constants.CHECKBOX_UNIQUE_YES) == self.constants.CHECKBOX_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.CHECKBOX_UNIQUE_YES)}"

    @log_decorator
    def verify_dropdown_select(self):
        """Verify DROPDOWN SELECT"""
        assert self.get_element_text(xpath=self.constants.SELECT_XPATH_GROUP) == self.constants.SELECT_XPATH_TEXT, \
            f"Actual: {self.get_element_text(xpath=self.constants.SELECT_XPATH_GROUP)}"
