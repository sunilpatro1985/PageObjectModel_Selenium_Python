import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


def test_Sample1():
    driver = webdriver.Chrome("/Users/skpatro/sel/chromedriver")
    # driver.maximize_window()
    driver.get("https://qavbox.github.io/demo/signup/")
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(50)
    assert "Registration" in driver.title
    action = ActionChains(driver)

    """
    el = driver.find_element_by_id("username")
    action.click(el).perform()
    time.sleep(3)
    action.send_keys("QAVBOX").perform()
    time.sleep(3)
    action.send_keys_to_element(el, "qavbox").perform()
    """
    
    """
    driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
    time.sleep(3)
    rightClickEl = driver.find_element_by_xpath("//span[contains(text(), 'right click me')]")
    action.context_click(rightClickEl).send_keys(Keys.ARROW_DOWN).pause(2)\
        .send_keys(Keys.ARROW_DOWN).pause(1).send_keys(Keys.ENTER).perform()
    """
    username = driver.find_element_by_id("username")
    email = driver.find_element_by_id("email")
    # action.move_to_element(username).click().send_keys("WATCH_QAVBOX").perform()
    username.send_keys("QAVBOX")
    action.key_down(Keys.COMMAND).key_down("A").key_up(Keys.COMMAND).perform()
    time.sleep(2)
    action.key_down(Keys.COMMAND).key_down("C").key_up(Keys.COMMAND).perform()
    time.sleep(2)
    action.click(email).key_down(Keys.COMMAND).key_down("V").key_up(Keys.COMMAND).perform()
    time.sleep(3)
    driver.quit()