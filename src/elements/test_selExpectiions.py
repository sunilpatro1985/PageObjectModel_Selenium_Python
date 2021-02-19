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

    el = driver.find_element_by_id("username")
    el.click()
    driver.refresh()
    try:
        el.send_keys("QAVBOX")
    except StaleElementReferenceException:
        el = driver.find_element_by_id("username")
        el.send_keys("QAVBOX")

    """
    try:
        el = driver.find_element_by_id("lblname")
        assert "Full Name1" in el.text
    except AssertionError:
        print(traceback.format_exc())

    try:
        username = driver.find_element_by_id("username1")
        username.send_keys("QAVBOX")
        assert "QAVBOX" in username.text
    except NoSuchElementException:
        print(traceback.format_exc())

    driver.find_element_by_id("email").send_keys("qavbox@gmail.com")
    """
    """"
    driver.find_element_by_id("username").click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())  # timeoutexception
    driver.switch_to.alert.accept()  # nosuchalertpresentexception
    """

    time.sleep(3)
    driver.quit()
