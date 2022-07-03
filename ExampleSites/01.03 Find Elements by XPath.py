from selenium import webdriver

chrome_driver_path = "/Users/alex/Downloads/chromedriver"

driver = webdriver.Chrome(chrome_driver_path)

demo_website = "file:/Users/alex/Downloads/01 demo-website.html"

driver.get(demo_website)

driver.maximize_window()

#form_element = driver.find_element_by_xpath("/html/body/form[1]")

#form_element = driver.find_element_by_xpath("//form[1]")

form_element = driver.find_element_by_xpath("//form[@id='demo-form']")

print(form_element.get_attribute("innerHTML"))

#driver.close()