from src.pom import settings
from src.pom.tests.base_test import BaseTest


class TestLogin(BaseTest):

    def test_valid_login(self):
        # launch url
        self.loginPage.login(settings.username, settings.password)
        self.homePage.wait_for_product_text()

    def test_locked_user_login(self):
        self.loginPage.login(settings.locked_username, settings.password)
        # self.homePage.wait_for_product_text()
        assert "Epic sadface: Sorry, this user has been locked out" \
               in self.loginPage.get_locked_error_text()

    def test_invalid_login(self):

        """
        assert "Epic sadface: Username and password do not match any user in this service" \
               in self.loginPage.get_locked_error_text()
        """
