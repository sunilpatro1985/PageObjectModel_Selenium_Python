import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_Sample1():
    driver = webdriver.Chrome("/Users/skpatro/sel/chromedriver")
    # driver.maximize_window()
    driver.get("https://qavbox.github.io/demo/delay/")
    # driver.implicitly_wait(30)
    # driver.set_page_load_timeout(50)
    assert "Delay" in driver.title

    commit = driver
    commit.click()
    # time.sleep(6)

    # delayEl = driver.find_element_by_id("delay")
    # print(delayEl.text)
    driver.find_element_by_css_selector("[value=''Click me!]").click()
    el = driver.find_element_by_id("two")
    print("First attempt - " + el.text)

    # WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(By.XPATH, "//p[@id='']"), "Submitted")

    driver.implicitly_wait(0)
    WebDriverWait(driver, 10).until(wait_till_text_appears((By.XPATH, "//p[@id='two']"), "here!"))
    # WebDriverWait(driver, 10).until(wait_till_text_appears(By.XPATH("//p[@id='two']"), "here!"))
    print("After waiting - " + driver.find_element_by_id("two").text)
    """
    time.sleep(6)
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//p[@id='two']")))
    print("First attempt - " + element.text)
    """

    time.sleep(3)
    driver.quit()


class wait_till_text_appears(object):

    def __init__(self, locator, text_):
        self.locator = locator
        self.text = text_

    def __call__(self, driver):
        try:
            element_text = driver.find_element(*self.locator).text
            print("Polllllllll" + element_text)
            return self.text in element_text
        except BaseException:
            return False

