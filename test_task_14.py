import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    for i in driver.find_elements_by_css_selector('i[class = "fa fa-external-link"]'):
        # кликаем кнопку, которая открывает новое окно
        i.click()
        # ждем появления нового окна, с новым идентификатором
        wait.until(EC.new_window_is_opened(old_windows))
        # запоминаем новые окна
        new_windows = driver.window_handles
        # вычленяем новое окно
        result = list(set(new_windows) - set(old_windows))
        new_window = result[0]
        # переключаемся в новое окно
        driver.switch_to.window(new_window)
        # закрываем его
        driver.close()
        # и возвращаемся в исходное окно
        driver.switch_to_window(main_window)
