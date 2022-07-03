from selenium import webdriver
import time # for time.sleep()

chrome_driver_path = '/Users/omboi/VSCode/chromedriver'

driver = webdriver.Chrome(chrome_driver_path)

demo_website = 'file:/Users/omboi/VSCode/Selenium/ExampleSites/01 demo-website.html'
website = 'https://www.google.com/?client=safari'

driver.get(demo_website)
driver.maximize_window()

time.sleep(5) # import time

driver.close()