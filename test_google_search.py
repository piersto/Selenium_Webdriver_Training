import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


class MyListener(AbstractEventListener):
    def before_find(self, by, value, driver):
        print(by, value)
    def after_find(self, by, value, driver):
        print(by, value, "found")
    def on_exception(self, exception, driver):
        print(exception)


@pytest.fixture
def driver(request):
    wd = EventFiringWebDriver(webdriver.Chrome(), MyListener())
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://google.com/")
    driver.find_element_by_name("q").send_keys('webdriver')
    driver.implicitly_wait(30)
    driver.find_element_by_name("btnK").click()
    WebDriverWait(driver, 10).until(EC.title_is('webdriver - Google Search'))
