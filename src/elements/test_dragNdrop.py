import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


def test_Sample1():
    driver = webdriver.Chrome("/Users/skpatro/sel/chromedriver")
    # driver.maximize_window()
    driver.get("https://qavbox.github.io/demo/")
    driver.find_element_by_css_selector(".myhmenu [href=\"/demo/dragndrop\"]").click()
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(50)
    assert "DragnDrop" in driver.title
    
    action = ActionChains(driver)
    source = driver.find_element_by_id("draggable")
    target = driver.find_element_by_id("droppable")
    action.drag_and_drop(source, target).perform()
    # action.click_and_hold(source).pause(2).move_to_element(target).perform()
    # action.click_and_hold(source).pause(2).move_to_element_with_offset(target, 100, 100).perform()
    # action.drag_and_drop_by_offset(source, 170, 10).perform()
    time.sleep(2)
    print(target.text)
    assert "Dropped!" in target.text
    driver.save_screenshot("/Users/skpatro/sel/dragndrop.png")
    driver.quit()
