import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException



@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_read_countries_table(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys('admin')
    driver.find_element_by_name("password").send_keys('admin')
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(EC.title_is('My Store'))

    driver.find_element_by_css_selector("li a[href$='countries&doc=countries']").click()
    wait = WebDriverWait(driver, 10)  # seconds
    wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(., 'Countries')]")))

    table = driver.find_element_by_css_selector('tbody')
    rows = table.find_elements_by_css_selector('tr.row')
    for row in rows:
        cell = row.find_elements_by_css_selector('td')
        code = cell[3].text
        name = cell[4].text
        print(code + " | " + name)


def test_read_zones_table(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys('admin')
    driver.find_element_by_name("password").send_keys('admin')
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(EC.title_is('My Store'))

    driver.find_element_by_css_selector("li a[href$='geo_zones&doc=geo_zones']").click()
    wait = WebDriverWait(driver, 10)  # seconds
    wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(., 'Geo Zones')]")))
    driver.get('http://localhost/litecart/admin/?app=geo_zones&doc=edit_geo_zone&page=1&geo_zone_id=1')

    zones_list = []
    table = driver.find_element_by_css_selector('#table-zones')
    rows = table.find_elements_by_css_selector('tr')
    for row in rows:
        try:
            cell = row.find_element_by_css_selector("td:nth-of-type(3) select option[selected]")
            name = cell.get_attribute('textContent')
            zones_list.append(name)

        except NoSuchElementException:
            pass  # не найден ну и ладно
        print(zones_list)
    #assert zones_list == sorted(zones_list)


def test_read_zones_table_1(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys('admin')
    driver.find_element_by_name("password").send_keys('admin')
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(EC.title_is('My Store'))

    driver.find_element_by_css_selector("li a[href$='geo_zones&doc=geo_zones']").click()
    wait = WebDriverWait(driver, 10)  # seconds
    wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(., 'Geo Zones')]")))
    driver.get('http://localhost/litecart/admin/?app=geo_zones&doc=edit_geo_zone&page=1&geo_zone_id=1')

    zones_list = []
    for element in driver.find_elements_by_css_selector("#table-zones tr td:nth-of-type(3) select option[selected]"):
        try:
            name = element.get_attribute('textContent')
            zones_list.append(name)

        except NoSuchElementException:
            pass  # не найден ну и ладно
        print(zones_list)
    #assert zones_list == sorted(zones_list)


