import time

import pytest

from src.pom import settings
from src.pom.tests.base_test import BaseTest
from src.pom.utility import xlReader


class TestHomePage(BaseTest):

    def test_product_sorting(self):
        self.loginPage.login(settings.username, settings.password)
        self.homePage.wait_for_product_text()

        xlReader.load_excel("/Users/skpatro/PycharmProjects/SampleSelPython/test_data.xlsx", "prodsort")
        data = xlReader.get_data_as_list_tuples()
        #  print(data)

        for item in data:
            self.homePage.select_item(item[0])
            time.sleep(1)
            assert self.homePage.get_first_item_name() == item[1]
            assert self.homePage.get_first_item_price() == ('$'+str(item[2]))
            time.sleep(1)

        time.sleep(2)

    @pytest.mark.skip
    def test_products_cart_count(self):
        # login
        self.loginPage.login(settings.username, settings.password)
        self.homePage.wait_for_product_text()

        # verify the product count
        print("Product count - " + str(self.homePage.get_items_count()))
        assert self.homePage.get_items_count() == 6

        # add couple of items and verify the cart count
        self.homePage.add_all_items_to_cart()
        print("cart count - " + self.homePage.get_cart_count())
        assert self.homePage.get_cart_count() == '6'
        time.sleep(3)

        # remove products from cart, verify the updated count
        self.homePage.remove_first_item_from_cart()
        self.homePage.remove_second_item_from_cart()
        assert self.homePage.get_cart_count() == '4'

        time.sleep(3)


