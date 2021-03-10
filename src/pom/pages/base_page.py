from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click(self, by_locator):
        # self.driver.
        self.wait.until(EC.presence_of_element_located(by_locator)).click()

    def send_keys(self, by_locator, value):
        # self.wait.until(EC.element_to_be_clickable(by_locator)).send_keys(value)
        self.wait.until(EC.presence_of_element_located(by_locator)).send_keys(value)

    def get_text(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator)).get_attribute("innerText")

    def wait_for(self, by_locator):
        self.wait.until(EC.visibility_of_element_located(by_locator))
