from selenium.webdriver.common.by import By

from src.pom.pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    username = (By.ID, "user-name")
    password = (By.ID, "password")
    loginButton = (By.ID, "login-button")
    locked_error_text = (By.CSS_SELECTOR, "h3[data-test='error']")

    def login(self, username, password):
        self.send_keys(self.username, username)
        self.send_keys(self.password, password)
        self.click(self.loginButton)

    def get_locked_error_text(self):
        return self.get_text(self.locked_error_text)
