from selenium.webdriver.common.by import By

from src.pom.pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    products_text = (By.CSS_SELECTOR, "div[class='product_label']")
    inventoryItems = (By.CSS_SELECTOR, ".inventory_item")
    cart_count = (By.CLASS_NAME, "shopping_cart_badge")
    remove_first_item = (By.CSS_SELECTOR, ".inventory_item:nth-child(1) .btn_inventory")
    remove_second_item = (By.CSS_SELECTOR, ".inventory_item:nth-child(2) .btn_inventory")
    sort_selector = (By.CSS_SELECTOR, ".product_sort_container")
    first_item_name = (By.CSS_SELECTOR, ".inventory_item:nth-child(1) .inventory_item_name")
    first_item_price = (By.CSS_SELECTOR, ".inventory_item:nth-child(1) .inventory_item_price")

    def wait_for_product_text(self):
        self.wait_for(self.products_text)

    def get_items_count(self):
        return self.get_count(self.inventoryItems)

    def add_all_items_to_cart(self):
        for i in range(1, self.get_items_count()+1):
            self.click((By.CSS_SELECTOR, ".inventory_item:nth-child("+str(i)+") .btn_inventory"))

    def get_cart_count(self):
        return self.get_text(self.cart_count)

    def remove_first_item_from_cart(self):
        self.click(self.remove_first_item)

    def remove_second_item_from_cart(self):
        self.click(self.remove_second_item)

    def select_item(self, option):
        self.select_by_text(self.sort_selector, option)

    def get_first_item_name(self):
        return self.get_text(self.first_item_name)

    def get_first_item_price(self):
        return self.get_text(self.first_item_price)