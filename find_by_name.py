from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time # for time.sleep()

chrome_driver_path = Service('/Users/omboi/VSCode/chromedriver')

driver = webdriver.Chrome(service=chrome_driver_path)

demo_website = 'file:/Users/omboi/VSCode/Selenium/ExampleSites/01 demo-website.html'
website = 'https://www.google.com/?client=safari'

driver.get(demo_website)
# driver.maximize_window()




# ----- Find by type 'name' name="demo-submission-name"
input_field = driver.find_element(By.NAME, 'demo-submission-name')
input_field.send_keys('Hello')
time.sleep(2)
input_field.submit() # submit input field


time.sleep(20) # import time
driver.close()