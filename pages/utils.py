import datetime
import logging
import random
import string
from time import sleep

from constants.create_post_page import CreatePostPageConsts


def random_num():
    """Generate random number"""
    return str(random.randint(111111, 999999))


def random_num_len(frn=1, ton=9):
    """Generate random number"""
    return str(random.randint(frn, ton))


def random_str(length=5):
    """Generate random string"""
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def wait_until_ok(timeout=5, period=0.5):
    """Reties until OK"""

    log = logging.getLogger("[WaitUntilOk]")

    def decorator(original_function):
        def wrapper(*args, **kwargs):
            end_time = datetime.datetime.now() + datetime.timedelta(seconds=timeout)
            while True:
                try:
                    return original_function(*args, **kwargs)
                except Exception as err:
                    if datetime.datetime.now() > end_time:
                        log.error(f"Catch: {err}")
                        raise err
                    sleep(period)

        return wrapper

    return decorator


def log_decorator(original_function):
    """Logging actions using docstrings"""

    log = logging.getLogger("[LogDecorator]")

    def wrapper(*args, **kwargs):
        result = original_function(*args, **kwargs)
        log.info(f"{original_function.__doc__}")
        return result

    return wrapper


class User:

    def __init__(self, username="", email="", password=""):
        self.username = username
        self.email = email
        self.password = password

    def fill_data(self, username="", email="", password=""):
        """Fill user with sample data and values if provided"""
        user = random_str()
        self.username = f"{user}{random_num()}" if not username else username
        self.email = f"{user}{random_num()}@mail.com" if not email else email
        self.password = f"{random_str(6)}{random_num()}" if not password else password

    def fill_data1(self, username="", email="", password=""):
        """Fill user with sample data (with error) and values if provided"""
        """Fill fields: email(as expected), login(incorrectly: too short) and password (as expected)"""
        user = random_str(length=1)
        self.username = f"{user}{random_num_len()}" if not username else username
        self.email = f"{user}{random_num()}@mail.com" if not email else email
        self.password = f"{random_str(6)}{random_num()}" if not password else password

    def fill_data2(self, username="", email="", password=""):
        """Fill user with sample data (with error) and values if provided"""
        """- Fill registration login (incorrectly: more than 30 characters)
            - Fill registration email (correctly)
            - Fill registration password (correctly)"""
        user = random_str(length=31)
        self.username = f"{user}{random_num()}" if not username else username
        self.email = f"{user}{random_num()}@mail.com" if not email else email
        self.password = f"{random_str(6)}{random_num()}" if not password else password

    def fill_data3(self, username="", email="", password=""):
        """Fill user with sample data (with error) and values if provided"""
        """- Fill registration login (incorrectly: insert space)
            - Fill registration email (correctly)
            - Fill registration password (correctly)"""
        user = random_str()
        self.username = f"{user}  {random_num()}" if not username else username
        self.email = f"{user}{random_num()}@mail.com" if not email else email
        self.password = f"{random_str(6)}{random_num()}" if not password else password

    def fill_data4(self, username="", email="", password=""):
        """Fill user with sample data (with error) and values if provided"""
        """ - Fill registration login (incorrectly: special chars)
            - Fill registration email (correctly)
            - Fill registration password (correctly)"""
        user = random_str()
        self.username = f"{user},./!#{random_num()}" if not username else username
        self.email = f"{user}{random_num()}@mail.com" if not email else email
        self.password = f"{random_str(6)}{random_num()}" if not password else password

    def fill_data5(self, username="", email="", password=""):
        """Fill user with sample data (with error) and values if provided"""
        """- Fill registration login (correctly)
        - Fill registration email (correctly)
        - Fill registration password (too short incorrectly)"""
        user = random_str()
        self.username = f"{user}{random_num()}" if not username else username
        self.email = f"{user}{random_num()}@mail.com" if not email else email
        self.password = f"{random_str(3)}{random_num_len()}" if not password else password

    def fill_data6(self, username="", email="", password=""):
        """Fill user with sample data (with error) and values if provided"""
        """ - Fill registration login and email (correctly)
        - Fill registration password (incorrectly: more than 50 chars passwords)"""
        user = random_str()
        self.username = f"{user}{random_num()}" if not username else username
        self.email = f"{user}{random_num()}@mail.com" if not email else email
        self.password = f"{random_str(51)}{random_num_len(11, 99)}" if not password else password

    def fill_data7(self, username="", email="", password=""):
        """Fill user with sample data (with error) and values if provided"""
        """- Fill registration login & password (correctly)
        - Fill registration email (incorrectly)"""
        user = random_str()
        self.username = f"{user}{random_num()}" if not username else username
        self.email = f"{user}{random_num()}random" if not email else email
        self.password = f"{random_str(6)}{random_num()}" if not password else password

    def fill_data8(self, username="", email="", password=""):
        """Fill user with sample data (with error) and values if provided"""
        """- Fill registration login & password (correctly)
        - Fill registration email (incorrectly)"""
        user = random_str()
        self.username = f"{user}{random_num()}" if not username else username
        self.email = f"{user}{random_num()}_random.com" if not email else email
        self.password = f"{random_str(6)}{random_num()}" if not password else password

    def fill_data9(self, username="", email="", password=""):
        """Fill user with sample data (with error) and values if provided"""
        """- Fill registration login & password (correctly)
        - Fill registration email (incorrectly)"""
        user = random_str()
        self.username = f"{user}{random_num()}" if not username else username
        self.email = f"{user}{random_num()}@mail54237example." if not email else email
        self.password = f"{random_str(6)}{random_num()}" if not password else password


class Post:

    def __init__(self, title="", body="", unique=False, option=CreatePostPageConsts.OPTION_ALL_USERS_TEXT):
        self.title = title
        self.body = body
        self.unique = unique
        self.option = option

    def fill_default(self):
        """Fill fields using random data"""
        self.title = random_str(15)
        self.body = random_str(200)
