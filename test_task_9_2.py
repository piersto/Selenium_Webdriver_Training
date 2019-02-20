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


def test_zones_are_sorted(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys('admin')
    driver.find_element_by_name("password").send_keys('admin')
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(EC.title_is('My Store'))

    driver.find_element_by_css_selector("li a[href$='geo_zones&doc=geo_zones']").click()
    wait = WebDriverWait(driver, 10)  # seconds
    wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(., 'Geo Zones')]")))

    elements = driver.find_elements_by_xpath("tr[contains(@class, 'row')]")
    for element in range(len(elements)):
        elements[element].click()
        wait = WebDriverWait(driver, 10)  # seconds
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
        time.sleep(2)

        zones_list = []
        table = driver.find_element_by_css_selector('#table-zones')
        rows = table.find_elements_by_name('zones')
        for row in rows:
            cell = row.find_element_by_css_selector("select[name='zones[1][zone_code]'")
            name = cell[2].get_attribute('innerText')
            zones_list.append(name)
        assert zones_list == sorted(zones_list)
