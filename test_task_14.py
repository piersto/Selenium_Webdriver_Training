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


def test_links_are_open_in_new_window(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys('admin')
    driver.find_element_by_name("password").send_keys('admin')
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(EC.title_is('My Store'))

    driver.get('http://localhost/litecart/admin/?app=countries&doc=countries')

    driver.find_element_by_css_selector("a[href$='country_code=CA']").click()

    main_window = driver.current_window_handle
    old_windows = driver.window_handles
    # открывает новое окно
    driver.find_element_by_css_selector("a[href='http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2']").click()
    # ожидание появления нового окна,
    # идентификатор которого отсутствует в списке oldWindows,
    # остаётся в качестве самостоятельного упражнения
    #new_window = wait.until(there_is_window_other_than(old_windows))
    driver.switch_to_window(new_window)
    # ...
    driver.close()
    driver.switch_to_window(main_window)

    time.sleep(3)

