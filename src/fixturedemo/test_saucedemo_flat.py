import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_SauceDemo:

    @pytest.mark.skip
    def test_saucedemo(self):
        driver = webdriver.Chrome("/Users/skpatro/sel/chromedriver")
        driver.get("https://www.saucedemo.com/index.html")
        driver.implicitly_wait(20)
        driver.find_element_by_id("user-name").send_keys("standard_user")
        # verify if the value typed correctly, assert the text
        driver.find_element_by_id("password").send_keys("secret_sauce")
        # print("secret - " + driver.find_element_by_id("password").get_attribute("value"))
        # verify if the value typed as , assert the text
        driver.find_element_by_id("login-button").click()
        # verify the button text

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='product_label']")))
        time.sleep(2)
        driver.quit()

    @pytest.mark.skip
    def test_itemcount(self):
        driver = webdriver.Chrome("/Users/skpatro/sel/chromedriver")
        driver.get("https://www.saucedemo.com/index.html")
        driver.implicitly_wait(20)
        driver.find_element_by_id("user-name").send_keys("standard_user")
        driver.find_element_by_id("password").send_keys("secret_sauce")
        driver.find_element_by_id("login-button").click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='product_label']")))

        # print(len(driver.find_elements_by_css_selector("div[class='inventory_item']")))
        item_count = len(driver.find_elements_by_css_selector("div[class='inventory_item']"))
        assert 6 == item_count
        time.sleep(2)
        driver.quit()