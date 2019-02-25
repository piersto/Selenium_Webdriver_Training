import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support.color import Color



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


def test_campaign_price_color(driver):
    driver.get("http://localhost/litecart/en/")
    WebDriverWait(driver, 10).until(EC.title_is('Online Store | My Store'))

    price_color_on_home_page = driver.find_element_by_css_selector('div#box-campaigns strong.campaign-price').value_of_css_property("color")
    print(Color.from_string(price_color_on_home_page).hex)
    print(price_color_on_home_page)

    '''blue_color_from_price = Color.from_string('blue').rgba
    green_color_from_price = Color.from_string('green').rgba
    blue = 0
    green = 0
    print(blue_color_from_price)
    assert blue_color_from_price == blue
    assert green_color_from_price == green'''''


def test_price_color(driver):
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

    assert campaign_price_color_on_home_page[1:3] == campaign_price_color


'''def test_campaign_price_color_martin(driver):
    driver.get("http://localhost/litecart/en/")
    WebDriverWait(driver, 10).until(EC.title_is('Online Store | My Store'))

    campaign_price_color_green = ' 0'
    campaign_price_color_blue = ' 0'
    campaign_price_color_on_home_page = driver.find_element_by_css_selector('div#box-campaigns strong.campaign-price').value_of_css_property("color")
    print(campaign_price_color_on_home_page)
    array_campaign_price_color_on_home_page = campaign_price_color_on_home_page.split(',')
    assert array_campaign_price_color_on_home_page[1] == campaign_price_color_green
    assert array_campaign_price_color_on_home_page[2] == campaign_price_color_blue'''


'''def test_removed_price_color(driver):
    driver.get("http://localhost/litecart/en/")
    WebDriverWait(driver, 10).until(EC.title_is('Online Store | My Store'))'''



print(Color.from_string('#00ff33').rgba)
print(Color.from_string('rgb(1, 255, 3)').hex)
print(Color.from_string('blue').rgba)
