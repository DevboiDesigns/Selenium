from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time # for time.sleep()
chrome_driver_path = Service('/Users/omboi/VSCode/chromedriver')
driver = webdriver.Chrome(service=chrome_driver_path)
demo_website = 'file:/Users/omboi/VSCode/Selenium/ExampleSites/01 demo-website.html'
website = 'https://www.google.com/'
driver.get(website)


# Find Input by Xpath
# ----------------------------------------------- id or name
input_field = driver.find_element(By.XPATH, "//input[@name='q']")
input_field.send_keys('Omboi music')
input_field.submit()

# ---- could not get to work on Google but above does 
# input_field = driver.find_element(By.XPATH, "//form[@role='search']/input[@name='q']")
#input_field.send_keys("Omboi music")



time.sleep(20)
driver.close()