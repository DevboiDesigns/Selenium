from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time # for time.sleep()
chrome_driver_path = Service('/Users/omboi/VSCode/chromedriver')
driver = webdriver.Chrome(service=chrome_driver_path)
demo_website = 'file:/Users/omboi/VSCode/Selenium/ExampleSites/01 demo-website.html'
website = 'https://www.youtube.com/'
driver.get(website)

# Find by Partial Link text
# ------------------- any amount of text in link text - must be element a(link)
partial_link_text = driver.find_element(By.PARTIAL_LINK_TEXT, "Zona")
partial_link_text.click()



time.sleep(20)
driver.close()