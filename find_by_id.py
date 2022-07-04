from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time # for time.sleep()
chrome_driver_path = Service('/Users/omboi/VSCode/chromedriver')
driver = webdriver.Chrome(service=chrome_driver_path)
demo_website = 'file:/Users/omboi/VSCode/Selenium/ExampleSites/01 demo-website.html'
driver.get(demo_website)

# By id
input_field = driver.find_element(By.ID, 'demo-submission-id')
input_field.send_keys('Devboi')
time.sleep(2)
input_field.submit()


time.sleep(20)
driver.close()