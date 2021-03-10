import time

import pytest
from selenium import webdriver

# browser = "chrome"
from src.pom import settings
from src.pom.pages.base_page import BasePage
from src.pom.pages.home_page import HomePage
from src.pom.pages.login_page import LoginPage

driver = None


def pytest_addoption(parser):
    # parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--browser", action="store", default=settings.browser)
    parser.addoption("--env", action="store", default=settings.env)


@pytest.fixture
def getBrowser(request):
    _browser = request.config.getoption("--browser")
    return _browser


@pytest.fixture
def getDriver(request, getBrowser):
    global driver
    print("browser from getBrowser method - " + getBrowser)
    if getBrowser == "chrome":
        driver = webdriver.Chrome("/Users/skpatro/sel/chromedriver")
    elif getBrowser == "firefox":
        driver = webdriver.Firefox(executable_path="/Users/skpatro/sel/geckodriver")
    # env = request.config.getoption("--env")
    # _driver.get("https://www." + env + ".saucedemo.com/index.html")
    driver.get(settings.url)
    driver.implicitly_wait(20)
    # request.cls.basePage = BasePage(driver)
    request.cls.loginPage = LoginPage(driver)
    request.cls.homePage = HomePage(driver)
    # request.cls.driver = _driver
    # yield request.cls.driver
    yield driver
    time.sleep(2)
    driver.quit()


