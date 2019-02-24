import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_first_item(driver):
    driver.get("http://localhost/litecart/en/")
    WebDriverWait(driver, 10).until(EC.title_is('Online Store | My Store'))

    name_on_home_page = driver.find_element_by_css_selector('div#box-most-popular div.name').text
    driver.find_element_by_css_selector('.product').click()
    name_on_product_page = driver.find_element_by_css_selector('div#box-product h1').text
    assert name_on_home_page == name_on_product_page



