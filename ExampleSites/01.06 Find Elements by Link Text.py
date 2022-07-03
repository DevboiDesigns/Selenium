from selenium import webdriver
import time 

chrome_driver_path = "/Users/alex/Downloads/chromedriver"

driver = webdriver.Chrome(chrome_driver_path)

demo_website = "file:/Users/alex/Downloads/01 demo-website.html"

driver.get(demo_website)

driver.maximize_window()

link_text = driver.find_element_by_link_text("Mammoth Interactive")

time.sleep(3)

link_text.click() 

time.sleep(3)

driver.close()