import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import string
import random


def random_string():
    # string will be chosen from letters, digits, len=3
    symbols = string.ascii_uppercase + string.digits
    return ''.join([random.choice(symbols) for i in range(3)])


@pytest.fixture
def driver(request):
    wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd


def test_first_item_name(driver):
    driver.get("http://localhost/litecart/en/")
    WebDriverWait(driver, 10).until(EC.title_is('Online Store | My Store'))

    driver.find_element_by_css_selector("td a[href$='create_account']").click()

    time.sleep(5)