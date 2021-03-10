from selenium.webdriver.common.by import By

from src.pom.pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    products_text = (By.CSS_SELECTOR, "div[class='product_label']")

    def wait_for_product_text(self):
        self.wait_for(self.products_text)

