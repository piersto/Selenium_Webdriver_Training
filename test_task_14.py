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
    wait = WebDriverWait(driver, 10)  # seconds

    driver.get('http://localhost/litecart/admin/?app=countries&doc=countries')

    driver.find_element_by_css_selector("a[href$='country_code=CA']").click()

    # запоминаем идентификатор текущего окна
    main_window = driver.current_window_handle
    # запоминаем идентификаторы уже открытых окон
    old_windows = driver.window_handles
    # кликаем кнопку, которая открывает новое окно
    driver.find_element_by_css_selector("a[href='http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2']").click()
    # ждем появления нового окна, с новым идентификатором
    new_window = wait.until(there_is_window_other_than(old_windows))
    # переключаемся в новое окно
    driver.switch_to.window(new_window)
    # закрываем его
    driver.close()
    # и возвращаемся в исходное окно
    driver.switch_to.window(main_window)

    time.sleep(3)


def there_is_window_other_than(driver, old_windows):
    new_windows = driver.window_handles
    wait = WebDriverWait(driver, 60)  # seconds
    wait.until(lambda d: len(old_windows) < len(new_windows))
    new_window = old_windows - new_windows
    return new_window
