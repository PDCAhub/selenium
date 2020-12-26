
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

with webdriver.Chrome() as driver:
    wait = WebDriverWait(driver, 10)
    action = webdriver.ActionChains(driver)
    driver.get("https://www.youtube.com")
    
    busqueda = driver.find_element_by_name('search_query')
    busqueda.send_keys("PDCAHUB eWelink node-red"+ Keys.ENTER)
    el = WebDriverWait(driver,timeout=30).until(lambda d: d.find_element_by_tag_name("p"))
    assert el.text == "Hello from JavaScript!"