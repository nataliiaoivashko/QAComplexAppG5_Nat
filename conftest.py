import pytest as pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.start_page import StartPage
from pages.utils import User


@pytest.fixture(scope="function")
def start_page():
    # Pre-conditions
    driver = webdriver.Chrome(DRIVER_PATH)
    driver.get(BASE_URL)
    driver.implicitly_wait(1)
    # Steps
    yield StartPage(driver)
    # Post-conditions
    driver.close()


@pytest.fixture()
def random_user():
    user = User()
    user.fill_data()
    return user


@pytest.fixture()
def random_user1():
    user = User()
    user.fill_data1()
    return user


@pytest.fixture()
def random_user2():
    user = User()
    user.fill_data2()
    return user


@pytest.fixture()
def random_user3():
    user = User()
    user.fill_data3()
    return user


@pytest.fixture()
def random_user4():
    user = User()
    user.fill_data4()
    return user


@pytest.fixture()
def random_user5():
    user = User()
    user.fill_data5()
    return user


@pytest.fixture()
def random_user6():
    user = User()
    user.fill_data6()
    return user


@pytest.fixture()
def random_user7():
    user = User()
    user.fill_data7()
    return user


@pytest.fixture()
def random_user8():
    user = User()
    user.fill_data8()
    return user


@pytest.fixture()
def random_user9():
    user = User()
    user.fill_data9()
    return user
