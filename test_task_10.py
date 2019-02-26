import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.color import Color


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_first_item_name(driver):
    driver.get("http://localhost/litecart/en/")
    WebDriverWait(driver, 10).until(EC.title_is('Online Store | My Store'))

    name_on_home_page = driver.find_element_by_css_selector('div#box-campaigns div.name').text
    driver.find_element_by_css_selector('div#box-campaigns .product').click()
    name_on_product_page = driver.find_element_by_css_selector('div#box-product h1').text
    assert name_on_home_page == name_on_product_page


def test_campaign_price(driver):
    driver.get("http://localhost/litecart/en/")
    WebDriverWait(driver, 10).until(EC.title_is('Online Store | My Store'))

    campaign_price_on_home_page = driver.find_element_by_css_selector('div#box-campaigns strong.campaign-price').text
    driver.find_element_by_css_selector('.product').click()

    campaign_price_on_product_page = driver.find_element_by_css_selector('div.price-wrapper strong.campaign-price').text
    assert campaign_price_on_home_page == campaign_price_on_product_page


def test_regular_price(driver):
    driver.get("http://localhost/litecart/en/")
    WebDriverWait(driver, 10).until(EC.title_is('Online Store | My Store'))

    price_on_home_page = driver.find_element_by_css_selector('div#box-campaigns s.regular-price').text
    driver.find_element_by_css_selector('div#box-campaigns .product').click()

    price_on_product_page = driver.find_element_by_css_selector('div.price-wrapper s.regular-price').text
    assert price_on_home_page == price_on_product_page


def test_campaign_price_color_on_home_page(driver):
    driver.get("http://localhost/litecart/en/")
    WebDriverWait(driver, 10).until(EC.title_is('Online Store | My Store'))

    get_color = driver.find_element_by_css_selector('div#box-campaigns strong.campaign-price').value_of_css_property("color")
    green_color_on_home_page = Color.from_string(get_color).hex[3:5]
    blue_color_on_home_page = Color.from_string(get_color).hex[5:7]
    green = '00'
    blue = '00'
    assert green_color_on_home_page == green
    assert blue_color_on_home_page == blue


def test_price_color_on_home_page(driver):
    driver.get("http://localhost/litecart/en/")
    WebDriverWait(driver, 10).until(EC.title_is('Online Store | My Store'))

    get_color = driver.find_element_by_css_selector('div#box-campaigns s.regular-price').value_of_css_property("color")
    red_color_on_home_page = Color.from_string(get_color).hex[1:3]
    green_color_on_home_page = Color.from_string(get_color).hex[3:5]
    blue_color_on_home_page = Color.from_string(get_color).hex[5:7]
    assert green_color_on_home_page == red_color_on_home_page
    assert blue_color_on_home_page == red_color_on_home_page
    assert green_color_on_home_page == blue_color_on_home_page


def test_campaign_price_color_on_product_page(driver):
    driver.get("http://localhost/litecart/en/")
    WebDriverWait(driver, 10).until(EC.title_is('Online Store | My Store'))

    driver.find_element_by_css_selector('div#box-campaigns .product').click()

    get_color = driver.find_element_by_css_selector('div.price-wrapper strong.campaign-price').value_of_css_property("color")
    green_color_on_product_page = Color.from_string(get_color).hex[3:5]
    blue_color_on_product_page = Color.from_string(get_color).hex[5:7]
    green = '00'
    blue = '00'
    assert green_color_on_product_page == green
    assert blue_color_on_product_page == blue


def test_price_color_on_product_page(driver):
    driver.get("http://localhost/litecart/en/")
    WebDriverWait(driver, 10).until(EC.title_is('Online Store | My Store'))

    driver.find_element_by_css_selector('div#box-campaigns .product').click()

    get_color = driver.find_element_by_css_selector('div.price-wrapper s.regular-price').value_of_css_property("color")
    red_color_on_product_page = Color.from_string(get_color).hex[1:3]
    green_color_on_product_page = Color.from_string(get_color).hex[3:5]
    blue_color_on_product_page = Color.from_string(get_color).hex[5:7]
    assert green_color_on_product_page == red_color_on_product_page
    assert blue_color_on_product_page == red_color_on_product_page
    assert green_color_on_product_page == blue_color_on_product_page


def test_campaign_price_bigger_than_price_on_home_page(driver):
    driver.get("http://localhost/litecart/en/")
    WebDriverWait(driver, 10).until(EC.title_is('Online Store | My Store'))

    campaign_price_on_home_page = driver.find_element_by_css_selector('div#box-campaigns strong.campaign-price').text[1:]
    price_on_home_page = driver.find_element_by_css_selector('div#box-campaigns s.regular-price').text[1:]
    print(campaign_price_on_home_page)
    print(price_on_home_page)
    assert float(campaign_price_on_home_page) < float(price_on_home_page)













