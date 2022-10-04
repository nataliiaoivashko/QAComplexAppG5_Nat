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

    def create_post_with_checkbox_dropdown(self, post):
        """Create post using provided values"""
        """Post Unique = YES and dropdown choice = ONE PERSON"""
        # filling the title and body of the post:
        self.fill_field(xpath=self.constants.TITLE_FIELD_XPATH, value=post.title)
        self.fill_field(xpath=self.constants.BODY_FIELD_XPATH, value=post.body)
        # checkbox unique post click-check:
        self.click(xpath=self.constants.CHECKBOX_UNIQUE_POST_INPUT_XPATH)
        # dropdown click and select of one option:
        self.click(xpath=self.constants.DROPDOWN_LIST_XPATH)
        self.click(self.constants.VISIBILITY_SELECTION_XPATH.format(option=self.constants.OPTION_ONE_PERSON_TEXT))
        self.click(xpath=self.constants.CREATE_POST_BUTTON_XPATH)

    @log_decorator
    def verify_checkbox(self):
        """Verify checkbox Unique"""
        assert self.get_element_text(self.constants.CHECKBOX_UNIQUE_YES) == self.constants.CHECKBOX_YES_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.CHECKBOX_UNIQUE_YES)}"

    @log_decorator
    def verify_dropdown_select(self):
        """Verify DROPDOWN SELECT"""
        assert self.get_element_text(xpath=self.constants.SELECTED_VISIBILITY_VALUE_XPATH) == \
               self.constants.OPTION_ONE_PERSON_TEXT, f"Actual:" \
                                                      f" {self.get_element_text(xpath=self.constants.SELECTED_VISIBILITY_VALUE_XPATH)}"

    @log_decorator
    def verify_post_title(self, post):
        """Verify post title"""
        assert self.get_element_text(xpath=self.constants.CREATED_TITLE_XPATH) == post.title, \
            f"Actual: {self.get_element_text(xpath=self.constants.CREATED_TITLE_XPATH)}"

    @log_decorator
    def verify_post_body(self, post):
        """Verify body"""
        assert self.get_element_text(
            xpath=self.constants.CREATED_BODY_CONTENT_XPATH.format(body=post.body)) == post.body
