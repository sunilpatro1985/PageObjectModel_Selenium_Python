import time

import pytest
from selenium import webdriver

browser = "chrome"


@pytest.fixture
def getBrowser():
    return browser


@pytest.fixture
def getDriver(request, getBrowser):
    _driver = None
    if getBrowser == "chrome":
        _driver = webdriver.Chrome("/Users/skpatro/sel/chromedriver")
    elif getBrowser == "firefox":
        pass
        # driver = webdriver.Firefox("/Users/skpatro/sel/geckodriver")
    _driver.get("https://www.saucedemo.com/index.html")
    _driver.implicitly_wait(20)
    request.cls.driver = _driver
    yield request.cls.driver
    time.sleep(2)
    request.cls.driver.quit()


