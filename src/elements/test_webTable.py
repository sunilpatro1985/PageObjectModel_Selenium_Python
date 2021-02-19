import time

from selenium import webdriver
from selenium.webdriver.support.select import Select


def test_Sample1():
    driver = webdriver.Chrome("/Users/skpatro/sel/chromedriver")
    # driver.maximize_window()
    driver.get("https://qavbox.github.io/demo/webtable/")
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(50)
    assert "webtable" in driver.title

    table = driver.find_element_by_id("table01")
    # header = table.find_elements_by_tag_name("th")
    body = table.find_element_by_tag_name("tbody")
    rows = body.find_elements_by_tag_name("tr")
    cells = body.find_elements_by_tag_name("td")

    print(len(rows))

    """
    for i in range(len(rows)):
        columns = rows[i].find_elements_by_tag_name("td")
        for j in range(len(columns)):
            if columns[j].text == "TFS":
                columns[0].click()
    """
    time.sleep(3)

    print(driver.find_element_by_xpath("//table['@id=table01']/tbody/tr[2]/td[3]").text)
    el = driver
    el.click()

    time.sleep(3)
    """
    for cell in cells:
        print(cell.text)
    """

    driver.quit()
