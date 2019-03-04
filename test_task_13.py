import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import os.path
import random
import string
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
    time.sleep(2)

    # Go back to Home page
    driver.find_element_by_css_selector("li a[href$='/litecart/en/']")

    add_element_to_the_basket(driver)
    time.sleep(2)

    # Go back to Home page
    driver.find_element_by_css_selector("li a[href$='/litecart/en/']")

    add_element_to_the_basket(driver)
    time.sleep(2)

# Go back to Home page
    #driver.find_element_by_css_selector("li a[href$='/litecart/en/']").click()

    driver.find_element_by_css_selector("a[href$='/en/checkout']").click()


def add_element_to_the_basket(driver):
    driver.get("http://localhost/litecart/en/")

    driver.find_element_by_css_selector('div#box-most-popular .product').click()

    quantity_start = driver.find_element_by_css_selector('span.quantity').text #0

    # Find out if element present
    if len(driver.find_elements_by_css_selector("[name='options[Size]']")) > 0:
        # If element is present, select 'Small' from drop-down menu
        Select(driver.find_element_by_name("options[Size]")).select_by_visible_text("Small")
    else:
        # If not present Click on 'Add to cart' button
        driver.find_element_by_name('add_cart_product').click()
        time.sleep(2)

    wait = WebDriverWait(driver, 10)  # seconds
    # обратите внимание, что локатор передается как tuple!
    element = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.quantity")))

    # Go back to Home page
    driver.find_element_by_css_selector("li a[href$='/litecart/en/']").click()


