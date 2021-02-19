import time
import traceback

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_Sample1():
    driver = webdriver.Chrome("/Users/skpatro/sel/chromedriver")
    # driver.maximize_window()
    driver.get("https://qavbox.github.io/demo/signup/")
    # driver.implicitly_wait(30)
    # driver.set_page_load_timeout(50)
    assert "Registration" in driver.title

    """
    el = driver.find_element_by_id("username")
    el.click()
    driver.refresh()
    try:
        el.send_keys("QAVBOX")
    except StaleElementReferenceException:
        el = driver.find_element_by_id("username")
        el.send_keys("QAVBOX")
    """

    click(driver, (By.ID, "username"))
    driver.refresh()
    send_Keys(driver, (By.ID, "username"), "QAVBOX")

    click(driver, (By.ID, "email"))
    send_Keys(driver, (By.ID, "email"), "qavbox@gmail.com")

    time.sleep(3)
    driver.quit()


def click(driver, locator):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator)).click()


def send_Keys(driver, locator, value):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator)).clear()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator)).send_keys(value)


def getText(driver, locator):
    pass