import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_template(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys('admin')
    driver.find_element_by_name("password").send_keys('admin')
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(EC.title_is('My Store'))

    #table = driver.find_element_by_id('box-apps-menu')
    elements = driver.find_elements_by_id("app-")
    for element in range(len(elements)):
        elements[element].click()
        wait = WebDriverWait(driver, 10)  # seconds
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
        time.sleep(2)
        elements = driver.find_elements_by_id("app-")
        '''sub_elements = driver.find_elements_by_css_selector('span.name')
        for sub_element in range(len(sub_elements)):
            sub_elements[sub_element].click()
            time.sleep(2)
            sub_elements = driver.find_elements_by_css_selector('span.name')'''
