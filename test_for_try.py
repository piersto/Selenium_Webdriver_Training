from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test(driver):
    driver.get("http://google.com")
    try:
        driver.find_element_by_css_selector("oooo")
    except NoSuchElementException:
        pass  # не найден ну и ладно

