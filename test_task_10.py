import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException



@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_first_item(driver):
    driver.get("http://localhost/litecart/en/")
    WebDriverWait(driver, 10).until(EC.title_is('Online Store | My Store'))

    name_on_home_page = driver.find_element_by_css_selector('div#box-most-popular div.name').text
    price = driver.find_element_by_css_selector()
    driver.find_element_by_css_selector('.product').click()
    name_on_product_page = driver.find_element_by_css_selector('div#box-product h1').text
    assert name_on_home_page == name_on_product_page


def test_first_price(driver):
    driver.get("http://localhost/litecart/en/")
    WebDriverWait(driver, 10).until(EC.title_is('Online Store | My Store'))

    try:
        price_on_home_page = driver.find_element_by_css_selector('div.price-wrapper span.price').text
    except NoSuchElementException:
        pass  # не найден ну и ладно

    campaign_price_on_home_page = driver.find_element_by_css_selector('div.price-wrapper strong.campaign-price').text

    driver.find_element_by_css_selector('.product').click()

    try:
        price_on_product_page = driver.find_element_by_css_selector('div.price-wrapper span.price').text
    except NoSuchElementException:
        pass  # не найден ну и ладно

    campaign_price_on_product_page = driver.find_element_by_css_selector('div.price-wrapper strong.campaign-price').text
    assert price_on_home_page == price_on_product_page
    assert campaign_price_on_home_page == campaign_price_on_product_page




