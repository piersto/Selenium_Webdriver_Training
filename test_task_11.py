import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import string
import random
from selenium.webdriver.support.select import Select


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def random_string():
    # string will be chosen from letters, digits, len=3
    symbols = string.ascii_lowercase + string.digits
    return ''.join([random.choice(symbols) for i in range(10)])




def test_create_account(driver):
    driver.get("http://localhost/litecart/en/")
    WebDriverWait(driver, 10).until(EC.title_is('Online Store | My Store'))
    test_data = random_string() + ('@') + random_string() + ('.com')

    driver.find_element_by_css_selector("td a[href$='create_account']").click()
    #First Name
    driver.find_element_by_name('firstname').send_keys('First_name')
    #Last Name
    driver.find_element_by_name('lastname').send_keys('Last_name')
    #Address 1
    driver.find_element_by_name('address1').send_keys('Address 1')
    #Postcode
    driver.find_element_by_name('postcode').send_keys('12345')
    #City
    driver.find_element_by_name('city').send_keys('New-York')
    #Country
    Select(driver.find_element_by_css_selector('select[name="country_code"]')).select_by_visible_text('United States')
    #Email
    email = driver.find_element_by_css_selector('input[name="email"]').send_keys(test_data)
    #Phone
    driver.find_element_by_name('phone').send_keys('1234567890')
    #Desired Password
    driver.find_element_by_name('password').send_keys('admin')
    #Confirm Password
    driver.find_element_by_name('confirmed_password').send_keys('admin')


    time.sleep(5)