import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    driver.get('http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1')
    product_links = driver.find_elements_by_css_selector("tr > td:nth-child(5) a[href*='product_id=']")
    for i in range(len(product_links)):
        product_links[i].click()
        for l in driver.get_log("browser"):
            print(l)
        driver.get('http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1')
        product_links = driver.find_elements_by_css_selector("tr > td:nth-child(5) a[href*='product_id=']")

