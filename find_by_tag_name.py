from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time # for time.sleep()
chrome_driver_path = Service('/Users/omboi/VSCode/chromedriver')
driver = webdriver.Chrome(service=chrome_driver_path)
demo_website = 'file:/Users/omboi/VSCode/Selenium/ExampleSites/01 demo-website.html'
website = 'https://www.youtube.com/'
driver.get(website)

# Find by Tag Name
# -------- will always return first element on page
button = driver.find_element(By.TAG_NAME, "button")
button.click()


time.sleep(20)
driver.close()