import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_links_are_open_in_new_window(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys('admin')
    driver.find_element_by_name("password").send_keys('admin')
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(EC.title_is('My Store'))
    wait = WebDriverWait(driver, 10)  # seconds

    driver.get('http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1')
    time.sleep(3)
    driver.find_element_by_css_selector("td:nth-child(2) a[href$='product_id=']").click()