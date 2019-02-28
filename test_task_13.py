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

    driver.find_element_by_css_selector('div#box-most-popular .product').click()

    driver.presence_of_element_located("[name='options[Size]']")

    Select(driver.find_element_by_name("options[Size]")).select_by_visible_text("Small")


    driver.find_element_by_name('add_cart_product').click()
    wait = WebDriverWait(driver, 10)  # seconds
    # обратите внимание, что локатор передается как tuple!
    element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='cart']//span[@class='quantity'][.='1']")))

    time.sleep(10)
