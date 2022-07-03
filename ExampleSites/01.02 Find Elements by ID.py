from selenium import webdriver
import time 

chrome_driver_path = "/Users/alex/Downloads/chromedriver"

driver = webdriver.Chrome(chrome_driver_path)

demo_website = "file:/Users/alex/Downloads/01 demo-website.html"

driver.get(demo_website)

driver.maximize_window()

input_field = driver.find_element_by_id("demo-submission-id")

time.sleep(2)

input_field.send_keys("12345")

time.sleep(2)

input_field.submit()