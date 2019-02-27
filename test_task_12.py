import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
import os.path
import random
import string


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def random_string():
    symbols = string.ascii_lowercase + string.digits
    return ''.join([random.choice(symbols) for i in range(1, 7)])


def test_item(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys('admin')
    driver.find_element_by_name("password").send_keys('admin')
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(EC.title_is('My Store'))

    driver.find_element_by_css_selector("li a[href$='/?app=catalog&doc=catalog']").click()
    wait = WebDriverWait(driver, 10)  # seconds
    wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(., 'Catalog')]")))

    driver.find_element_by_css_selector("a[href$='catalog&doc=edit_product']").click()
    driver.find_element_by_css_selector('input[value="1"]').click()

    test_data = 'Product name ' + random_string()
    product_name = test_data

    driver.find_element_by_css_selector('input[name="name[en]"]').send_keys(product_name)
    driver.find_element_by_css_selector('input[name="new_images[]"]').send_keys(os.getcwd() + "/picture.png")
    time.sleep(5)

    driver.find_element_by_css_selector("a[href='#tab-information']").click()
    time.sleep(1)

    Select(driver.find_element_by_css_selector('select[name="manufacturer_id"]')).select_by_visible_text('ACME Corp.')

    driver.find_element_by_css_selector('div.trumbowyg-editor').send_keys('bla bla bla')

    driver.find_element_by_css_selector('a[href="#tab-prices"]').click()
    time.sleep(1)

    driver.find_element_by_css_selector('input[name="purchase_price"]').clear()
    driver.find_element_by_css_selector('input[name="purchase_price"]').send_keys('10')

    driver.find_element_by_css_selector('button[name=save]')

    driver.find_element_by_css_selector(product_name).click()


    time.sleep(5)





