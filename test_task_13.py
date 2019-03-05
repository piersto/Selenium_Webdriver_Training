import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_add_product(driver):
    driver.get("http://localhost/litecart/en/")
    WebDriverWait(driver, 10).until(EC.title_is('Online Store | My Store'))

    add_element_to_the_basket(driver)

    add_element_to_the_basket(driver)

    add_element_to_the_basket(driver)

    # Go to the basket
    driver.find_element_by_css_selector("a[href$='/en/checkout']").click()

    buttons = driver.find_elements_by_css_selector("[name='remove_cart_item']")
    for button in buttons:
        if len(driver.find_elements_by_css_selector("td.item")) > 0:
            wait = WebDriverWait(driver, 10)  # seconds
            button = wait.until(EC.visibility_of_element_located((By.NAME, "remove_cart_item")))
            button.click()
            driver.find_elements_by_css_selector("[name='remove_cart_item']")

    # Go back to Home page
    driver.find_element_by_css_selector("li a[href$='/litecart/en/']").click()
    time.sleep(7)


def add_element_to_the_basket(driver):
    driver.find_element_by_css_selector('div#box-most-popular .product').click()

    quantity_start = driver.find_element_by_css_selector('span.quantity').text
    # Find out if element present
    if len(driver.find_elements_by_css_selector("[name='options[Size]']")) > 0:
        # If element is present, select 'Small' from drop-down menu
        Select(driver.find_element_by_name("options[Size]")).select_by_visible_text("Small")
        driver.find_element_by_name('add_cart_product').click()
    else:
        # If not present Click on 'Add to cart' button
        driver.find_element_by_name('add_cart_product').click()
        time.sleep(2)
    wait = WebDriverWait(driver, 10)  # seconds
    wait.until(lambda d: d.find_element_by_css_selector('span.quantity').text != quantity_start)

    # Go back to Home page
    driver.find_element_by_css_selector("li a[href$='/litecart/en/']").click()

