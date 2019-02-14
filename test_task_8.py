import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_stiker_presense(driver):
    driver.get("http://localhost/litecart/en/")
    WebDriverWait(driver, 10).until(EC.title_is('Online Store | My Store'))
    elements = driver.find_elements_by_css_selector('div.image-wrapper')
    sticker = driver.find_elements_by_css_selector('div.sticker')
    for sticker in elements:
        sticker = driver.find_element_by_css_selector('div.sticker')
        print(sticker)


