import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.fixturedemo.base_test import BaseTest


# @pytest.mark.usefixtures("getDriver")
class TestSauceDemo1(BaseTest):

    def test_itemcount(self):
        driver = self.driver
        driver.find_element_by_id("user-name").send_keys("standard_user")
        driver.find_element_by_id("password").send_keys("secret_sauce")
        driver.find_element_by_id("login-button").click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='product_label']")))

        # print(len(driver.find_elements_by_css_selector("div[class='inventory_item']")))
        item_count = len(driver.find_elements_by_css_selector("div[class='inventory_item']"))
        assert 6 == item_count


