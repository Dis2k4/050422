import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Firefox(firefox_binary="c:\\Program Files\\Mozilla Firefox\\firefox.exe")
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test1(driver):
    driver.get("https://www.wildberries.ru/")
    driver.find_element_by_id("searchInput").send_keys("webdriver")
    driver.find_element_by_id("applySearchBtn").click()
    WebDriverWait(driver, 10).until(EC.title_is("Wildberries - модный интернет магазин"))