import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.fixturedemo.base_test import BaseTest


# @pytest.mark.usefixtures("getDriver")
class Test_SauceDemo(BaseTest):

    def test_saucedemo(self):
        driver = self.driver
        driver.find_element_by_id("user-name").send_keys("standard_user")
        # verify if the value typed correctly, assert the text
        driver.find_element_by_id("password").send_keys("secret_sauce")
        # print("secret - " + driver.find_element_by_id("password").get_attribute("value"))
        # verify if the value typed as , assert the text
        driver.find_element_by_id("login-button").click()
        # verify the button text

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='product_label']")))

    def test_saucedemo1(self):
        driver = self.driver
        print(driver.title)


