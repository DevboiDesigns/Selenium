from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time # for time.sleep()
chrome_driver_path = Service('/Users/omboi/VSCode/chromedriver')
driver = webdriver.Chrome(service=chrome_driver_path)
demo_website = 'file:/Users/omboi/VSCode/Selenium/ExampleSites/01 demo-website.html'
website = 'https://www.google.com/'
driver.get(demo_website)

# By Xpath - index counting starts at 1
# form_element = driver.find_element(By.XPATH, '/html/body/form[1]')
# form_element = driver.find_element(By.XPATH, '//form[1]') # /(html)/(body)
form_element = driver.find_element(By.XPATH, "//form[@id='demo-form']") 
print(form_element.get_attribute('innerHTML'))

# ---------------------- PRINTS
# <label for="demo-submission">Make a test submission:</label>
# <input type="text" id="demo-submission-id" name="demo-submission-name">
# <input type="submit" value="Submit">

time.sleep(20)
driver.close()