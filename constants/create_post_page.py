class CreatePostPageConsts:
    TITLE_FIELD_XPATH = ".//input[@id='post-title']"
    BODY_FIELD_XPATH = ".//textarea[@id='post-body']"

    SUCCESS_MESSAGE_XPATH = ".//div[@class='alert alert-success text-center']"
    SUCCESS_MESSAGE_TEXT = "New post successfully created."

    CREATE_POST_BUTTON_XPATH = ".//button[@class='btn btn-primary']"

    CHECKBOX_INPUT_XPATH = ".//input[contains(@type,'checkbox')]"

    DROPDOWN_LIST_XPATH = ".//select[@name='select1']"

    OPTION_ALL_USERS = "All Users"
    OPTION_ONE_PERSON = "One Person"
    OPTION_GROUP_MESSAGE = "Group Message"
    VISIBILITY_SELECTION_XPATH = ".//option[@value='{option}']"

    SELECT_XPATH_GROUP = './/i'
    SELECT_XPATH_TEXT = "One Person"
    CHECKBOX_UNIQUE_YES = ".//p[contains(.,'Is this post unique? : yes')]"
    CHECKBOX_TEXT = "Is this post unique?: yes"

    # CHECKBOX_UNIQUE_NO = ".//p[contains(.,'Is this post unique? : no')]"
    # SELECT_XPATH_GROUP = ".//u[contains(.,'Group Message')]"
