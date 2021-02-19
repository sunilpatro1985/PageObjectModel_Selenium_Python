import pytest


@pytest.mark.usefixtures("getDriver")
class BaseTest:
    pass

    # def open(self, url):
        # self.driver.get(url)


