from selenium import webdriver
import time

chrome_driver_path = "/Users/alex/Downloads/chromedriver"

driver = webdriver.Chrome(chrome_driver_path)

demo_website = "file:/Users/alex/Downloads/01 demo-website.html"

driver.get(demo_website)

driver.maximize_window()

button = driver.find_element_by_tag_name("button")

time.sleep(3)

button.click()