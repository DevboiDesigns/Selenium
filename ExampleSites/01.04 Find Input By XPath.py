from selenium import webdriver
import time 

chrome_driver_path = "/Users/alex/Downloads/chromedriver"

driver = webdriver.Chrome(chrome_driver_path)

demo_website = "file:/Users/alex/Downloads/01 demo-website.html"

driver.get(demo_website)

#input_field = driver.find_element_by_xpath("//input[@name='demo-submission-name']")

#input_field = driver.find_element_by_xpath("//input[@id='demo-submission-id']")

input_field = driver.find_element_by_xpath("//form[@id='demo-form']/input[1]")

input_field.send_keys("hello")

time.sleep(2)

input_field.submit()

time.sleep(5)

driver.close()