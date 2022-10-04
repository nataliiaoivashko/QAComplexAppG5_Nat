import logging
from time import sleep

import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from constants.create_post_page import CreatePostPageConsts
from pages.start_page import StartPage
from pages.utils import Post, random_str


class TestCreatePostPage:
    log = logging.getLogger("[CreatePostPage]")

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

    @pytest.fixture()
    def hello_page(self, start_page, random_user):
        """Sign Up as the user and return the page"""
        return start_page.sign_up_and_verify(random_user)

    def test_create_post_page(self, hello_page):
        """
        - Pre-conditions:
            - Sign Up/Sign In as a user
        - Steps:
            - Navigate to create Post Page
            - Create Post
            - Verify the result
        """
        # Navigate to create Post Page
        create_post_page = hello_page.header.navigate_to_create_post_page()

        # Create Post
        post = Post()
        post.fill_default()
        create_post_page.create_post(post)

        # Verify the result
        create_post_page.verify_successfully_created()

    def test_create_complete_post_with_check_dropdown(self, hello_page):
        """
            - Pre-conditions:
            - Sign Up/Sign In as a user
            - Steps:
                - Fill title, body, select check box, choose visibility adn click on crete button
                - Verify that data match to expected
            """
        # Navigate to create Post Page
        create_post_page = hello_page.header.navigate_to_create_post_page()
        # Create Post
        post = Post()
        post.fill_default()
        create_post_page.create_post_with_checkbox_dropdown(post)
        sleep(1)
        # Verify the result
        create_post_page.verify_successfully_created()
        create_post_page.verify_post_title(post)
        create_post_page.verify_post_body(post)
        create_post_page.verify_checkbox()
        create_post_page.verify_dropdown_select()

    def test_create_full_post(self, hello_page):
        """
        - Pre-conditions:
            - Sign Up/Sign In as a user
        - Steps:
            - Fill title, body, select check box, choose visibility adn click on crete button
            - Verify that data match to expected
        """
        # Navigate to create Post Page
        create_post_page = hello_page.header.navigate_to_create_post_page()

        # Create Post
        post = Post(title=random_str(15), body=random_str(20), unique=True,
                    option=CreatePostPageConsts.OPTION_GROUP_MESSAGE_TEXT)
        create_post_page.create_full_post(post)

        # Verify the result
        create_post_page.verify_full_post_data(post)
