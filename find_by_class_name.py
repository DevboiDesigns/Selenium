from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time # for time.sleep()
chrome_driver_path = Service('/Users/omboi/VSCode/chromedriver')
driver = webdriver.Chrome(service=chrome_driver_path)
demo_website = 'file:/Users/omboi/VSCode/Selenium/ExampleSites/01 demo-website.html'
website = 'https://www.youtube.com/'
driver.get(website)


# Find by Class Name
# style-scope ytd-topbar-menu-button-renderer ------ class name of element
button = driver.find_element(By.CLASS_NAME, "style-scope ytd-topbar-menu-button-renderer")
button.click()


time.sleep(20)
driver.close()