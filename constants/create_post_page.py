class CreatePostPageConsts:
    TITLE_FIELD_XPATH = ".//input[@id='post-title']"
    BODY_FIELD_XPATH = ".//textarea[@id='post-body']"
    CREATE_POST_BUTTON_XPATH = ".//button[@class='btn btn-primary']"
    SUCCESS_MESSAGE_XPATH = ".//div[@class='alert alert-success text-center']"
    SUCCESS_MESSAGE_TEXT = "New post successfully created."
    CREATED_TITLE_XPATH = ".//h2"
    CREATED_BODY_CONTENT_XPATH = ".//div[@class='body-content']/p[contains(text(), '{body}')]"
    CHECKBOX_UNIQUE_POST_INPUT_XPATH = ".//input[contains(@type,'checkbox') and (@name='uniquePost')]"
    DROPDOWN_LIST_XPATH = ".//select[@name='select1']"  # click on the dropdown list
    VISIBILITY_SELECTION_XPATH = ".//option[@value='{option}']"  # choosing the option value from dropdown
    OPTION_ALL_USERS_TEXT = "All Users"  # dropdown option 1
    OPTION_ONE_PERSON_TEXT = "One Person"  # dropdown option 2
    OPTION_GROUP_MESSAGE_TEXT = "Group Message"  # dropdown option 3
    SELECTED_VISIBILITY_VALUE_XPATH = ".//u"  # this is the option that was selected
    CHECKBOX_UNIQUE_YES = ".//p[contains(.,'Is this post unique? : yes')]"  # when "yes" was selected
    CHECKBOX_UNIQUE_NO = ".//p[contains(.,'Is this post unique? : no')]"  # when "no" was selected
    CHECKBOX_YES_TEXT = "Is this post unique? : yes"
    CHECKBOX_NO_TEXT = "Is this post unique? : no"
    IS_POST_UNIQUE_XPATH = ".//p[contains(text(), 'Is this post unique?')]"
