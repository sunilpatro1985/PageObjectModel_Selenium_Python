from selenium import webdriver
import time

# driver = webdriver.Firefox(executable_path="C:\\Grid\\geckodriver.exe")
# driver = webdriver.Ie(executable_path="C:\\Grid\\IEdriverserver.exe")


class Test_global:
    driver = None


def test_Sample1():
    Test_global.driver = webdriver.Chrome("/Users/skpatro/sel/chromedriver")
    # driver.maximize_window()
    Test_global.driver.implicitly_wait(30)
    Test_global.driver.set_page_load_timeout(50)
    Test_global.driver.get("https://qavbox.github.io/demo")
    assert "QA1VBOX" in Test_global.driver.title


def test_navReg():
    # Test_global.driver.click()
    # driver.find_element_by_link_text("SignUp Form").click()
    Test_global.driver.save_screenshot("/Users/skpatro/sel/test.png")
    time.sleep(3)
    Test_global.driver.quit()