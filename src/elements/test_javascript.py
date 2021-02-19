import time

from selenium import webdriver
from selenium.webdriver.support.select import Select


def test_Sample1():
    driver = webdriver.Chrome("/Users/skpatro/sel/chromedriver")
    # driver.maximize_window()
    driver.get("https://qavbox.github.io/demo/signup/")
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(50)
    assert "Registration" in driver.title
    
    # print("Title - " + driver.execute_script("return document.title"))

    # print("URL - " + driver.execute_script("return document.URL"))

    # print("is Page loaded - " + driver.execute_script("return document.readyState"))

    """
    driver.execute_script("window.location = 'https://qavbox.github.io/demo/'")

    # using javascript, identify & click on the element
    element = driver.execute_script("return document.querySelector(\"[href='/demo/signup']\")")
    driver.execute_script("arguments[0].click();", element)
    """

    time.sleep(2)
    """
    driver.execute_script("return document.getElementById('username').value='qavbox'")
    time.sleep(4)

    print("Entered value - " + driver.execute_script("return document.getElementById('username').value"))
    """

    driver.execute_script("document.querySelector(\"input[value='seven']\").checked=true")
    time.sleep(5)

    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)
    driver.quit()
