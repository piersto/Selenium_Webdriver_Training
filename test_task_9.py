import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_areas_are_sorted(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys('admin')
    driver.find_element_by_name("password").send_keys('admin')
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(EC.title_is('My Store'))

    driver.find_element_by_css_selector("li a[href$='countries&doc=countries']").click()
    wait = WebDriverWait(driver, 10)  # seconds
    wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(., 'Countries')]")))

    elements = driver.find_elements_by_css_selector('tr.row td:nth-of-type(5)')
    for element in range(len(elements)):
        if driver.find_element_by_xpath("//td[.='0']"):
            pass
        else:
            elements[element].click()
            wait = WebDriverWait(driver, 10)  # seconds
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))

        zones_list = []
        assert zones_list == sorted(zones_list)
        print(zones_list)


def test_countries_are_sorted(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys('admin')
    driver.find_element_by_name("password").send_keys('admin')
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(EC.title_is('My Store'))

    driver.find_element_by_css_selector("li a[href$='countries&doc=countries']").click()
    wait = WebDriverWait(driver, 10)  # seconds
    wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(., 'Countries')]")))

    countries_list = []
    table = driver.find_element_by_css_selector('tbody')
    rows = table.find_elements_by_css_selector('tr.row')
    for row in rows:
        cell = row.find_elements_by_css_selector('td')
        name = cell[4].text
        countries_list.append(name)
    assert countries_list == sorted(countries_list)
    print(countries_list)

