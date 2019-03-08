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


def test_areas_are_sorted(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys('admin')
    driver.find_element_by_name("password").send_keys('admin')
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(EC.title_is('My Store'))

    driver.find_element_by_css_selector("li a[href$='countries&doc=countries']").click()
    wait = WebDriverWait(driver, 10)  # seconds
    wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(., 'Countries')]")))

    rows = driver.find_elements_by_css_selector("tr[class='row']")
    for i in range(len(rows)):
        zone_text = rows[i].find_element_by_css_selector("td:nth-child(6)").text
        if zone_text != "0":
            rows[i].find_element_by_css_selector('td:nth-child(5) > a').click()
            time.sleep(5)

            wait = WebDriverWait(driver, 10)  # seconds
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))

            zones_list = []
            for zone in driver.find_elements_by_css_selector('td:nth-child(3) > input[type="hidden"]'):
                try:
                    name = zone.get_attribute('value')
                    zones_list.append(name)

                except NoSuchElementException:
                    pass  # не найден ну и ладно
            assert zones_list == sorted(zones_list)

            print(zones_list)
            driver.find_element_by_css_selector("li a[href$='countries&doc=countries']").click()

            rows = driver.find_elements_by_css_selector("tr[class='row']")






'''

    #driver.find_element_by_xpath("//*[@id='content']/form/table/tbody/tr[2]//[not td[.='0']]")

    rows = driver.find_elements_by_css_selector("tr[class='row']")
    for i in range(len(rows)):
        row = rows[i]
        zone_text = row.find_element_by_css_selector("td:nth-child(6)").text
        if zone_text != "0":
            row.find_element_by_css_selector('td:nth-child(5) > a').click()
        else:
            pass
        time.sleep(3)

        wait = WebDriverWait(driver, 10)  # seconds
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
        driver.find_element_by_css_selector("li a[href$='countries&doc=countries']").click()''




        driver.find_element_by_css_selector("li a[href$='countries&doc=countries']").click()
        wait = WebDriverWait(driver, 10)  # seconds
        wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(., 'Countries')]")))
        # row = driver.find_element_by_xpath("//*[@id='content']/form/table/tbody/tr[2]//td[.='0']")
        elements = driver.find_elements_by_css_selector('tr.row td:nth-of-type(5) a[href]')

    #row = driver.find_element_by_xpath("//*[@id='content']/form/table/tbody/tr[2]//td[.='0']")
    elements = driver.find_elements_by_css_selector('tr.row td:nth-of-type(5) a[href]')
    for element in range(len(elements)):
        if not driver.find_element_by_xpath("//*[@id='content']/form/table/tbody/tr[2]//td[.='0']"):
            elements[element].click()
            time.sleep(2)
            wait = WebDriverWait(driver, 10)  # seconds
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
            driver.find_element_by_css_selector("li a[href$='countries&doc=countries']").click()
            wait = WebDriverWait(driver, 10)  # seconds
            wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(., 'Countries')]")))
            #row = driver.find_element_by_xpath("//*[@id='content']/form/table/tbody/tr[2]//td[.='0']")
            elements = driver.find_elements_by_css_selector('tr.row td:nth-of-type(5) a[href]')


def test_areas_are_sorted(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys('admin')
    driver.find_element_by_name("password").send_keys('admin')
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(EC.title_is('My Store'))

    driver.find_element_by_css_selector("li a[href$='countries&doc=countries']").click()
    wait = WebDriverWait(driver, 10)  # seconds
    wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(., 'Countries')]")))

    rows = driver.find_elements_by_css_selector("tr.row")

    for row in range (len (rows)):
        last_row = row
        tds = rows[row].find_elements_by_tag_name("td")
        if (tds[5].text != "0"):
            tds[4].find_element_by_css_selector('a[href]').click()
            driver.find_element_by_css_selector("li a[href$='countries&doc=countries']").click()
            row = last_row
            rows = driver.find_elements_by_css_selector("tr.row")


row = driver.find_element_by_xpath("//*[@id='content']/form/table/tbody/tr[2]//td[.='0']")
    elements = driver.find_elements_by_css_selector('tr.row td:nth-of-type(5) a[href]')
    for element in range(len(elements)):
        elements[element].click()
        time.sleep(2)
        wait = WebDriverWait(driver, 10)  # seconds
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
        driver.find_element_by_css_selector("li a[href$='countries&doc=countries']").click()
        wait = WebDriverWait(driver, 10)  # seconds
        wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(., 'Countries')]")))
        #row = driver.find_element_by_xpath("//*[@id='content']/form/table/tbody/tr[2]//td[.='0']")
        elements = driver.find_elements_by_css_selector('tr.row td:nth-of-type(5) a[href]')'''


'''zones_list = []
assert zones_list == sorted(zones_list)
print(zones_list)'''


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

