import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_sticker_presence(driver):
    driver.get("http://localhost/litecart/en/")
    WebDriverWait(driver, 10).until(EC.title_is('Online Store | My Store'))

    products = driver.find_elements_by_css_selector('.image-wrapper')
    for sticker in products:
        sticker = driver.find_elements_by_css_selector('.sticker')
        assert len(products) == len(sticker)
        print(sticker)
