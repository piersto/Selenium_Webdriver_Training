import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time


@pytest.fixture
def driver(request):
    wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd


def test_first_item_name(driver):
    driver.get("http://localhost/litecart/en/")
    WebDriverWait(driver, 10).until(EC.title_is('Online Store | My Store'))

    name_on_home_page = driver.find_element_by_css_selector('div#box-campaigns div.name').text
    driver.find_element_by_css_selector('div#box-campaigns .product').click()
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


'''def test_price_color(driver):
    driver.get("http://localhost/litecart/en/")
    WebDriverWait(driver, 10).until(EC.title_is('Online Store | My Store'))

    try:
        price_color_on_home_page = driver.find_element_by_css_selector('div.price-wrapper span.price').value_of_css_property("color")
        price_color = (0, 0)
        assert price_color_on_home_page[0:-1] == price_color
    except NoSuchElementException:
        pass  # не найден ну и ладно
    price_color = (0, 0)
    campaign_price_color = (0, 0)
    campaign_price_color_on_home_page = driver.find_element_by_css_selector('div.price-wrapper strong.campaign-price').value_of_css_property("color")
    print(campaign_price_color_on_home_page)
    time.sleep(3)

    assert campaign_price_color_on_home_page[1:3] == campaign_price_color'''


def test_campaign_price_color(driver):
    driver.get("http://localhost/litecart/en/")
    WebDriverWait(driver, 10).until(EC.title_is('Online Store | My Store'))

    campaign_price_color_green = ' 0'
    campaign_price_color_blue = ' 0'
    campaign_price_color_on_home_page = driver.find_element_by_css_selector('div.price-wrapper strong.campaign-price').value_of_css_property("color")
    print(campaign_price_color_on_home_page)
    array_campaign_price_color_on_home_page = campaign_price_color_on_home_page.split(',')
    assert array_campaign_price_color_on_home_page[1] == campaign_price_color_green
    assert array_campaign_price_color_on_home_page[2] == campaign_price_color_blue


def test_removed_price_color(driver):
    driver.get("http://localhost/litecart/en/")
    WebDriverWait(driver, 10).until(EC.title_is('Online Store | My Store'))
