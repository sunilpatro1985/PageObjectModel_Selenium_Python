from selenium import webdriver
from selenium.webdriver.support.select import Select


def test_Sample1():
    driver = webdriver.Chrome("/Users/skpatro/sel/chromedriver")
    # driver.maximize_window()
    driver.get("https://qavbox.github.io/demo/signup/")
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(50)
    assert "Registration" in driver.title
    select = Select(driver.find_element_by_name("sgender"))
    # select.select_by_visible_text("Male")
    # select.select_by_value("female")
    select.select_by_index(3)
    # index starts from 0
    print("\nSelected item - " + select.first_selected_option.text)
    assert "Not Applicable" in select.first_selected_option.text

    opts = select.options
    print("Dropdown options are - ")
    for opt in opts:
        print(opt.text)
    driver.quit()