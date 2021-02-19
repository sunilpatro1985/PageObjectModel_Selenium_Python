import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


def test_Sample1():
    driver = webdriver.Chrome("/Users/skpatro/sel/chromedriver")
    # driver.maximize_window()
    driver.get("https://qavbox.github.io/demo/dragndrop/")
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(50)
    # assert "DragnDrop" in driver.title
    time.sleep(2)
    
    action = ActionChains(driver)
    source = driver.find_element_by_id("draggable")
    target = driver.find_element_by_id("droppable")
    # action.drag_and_drop_by_offset(source, 168, 4).perform()

    action.click_and_hold(driver.find_element_by_id("draggable"))\
        .move_to_element_with_offset(driver.find_element_by_id("droppable"), 10, 13).perform()
    # action.drag_and_drop(source, target).perform()
    time.sleep(2)
    print(driver.find_element_by_id("dropText").text)
    # assert "Dropped!" in driver.find_element_by_id("dropText").text
    driver.save_screenshot("/Users/skpatro/sel/dragnDrop.png")
    driver.quit()