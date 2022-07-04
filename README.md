# Selenium Web Driver

- **work in progress**
- [Selenium Docs](https://www.selenium.dev/documentation/)
- 'Scraping'

## Install

- `pip3 install --upgrad pip`
- `pip3 install selenium`
- Web Driver
  - [Chrome](https://chromedriver.chromium.org/downloads)
  - [Firefox](https://github.com/mozilla/geckodriver)

# Setup

```py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time # for time.sleep()

chrome_driver_path = Service('/Users/omboi/VSCode/chromedriver')

driver = webdriver.Chrome(service=chrome_driver_path)

demo_website = 'file:/Users/omboi/VSCode/Selenium/ExampleSites/01 demo-website.html'
```

## Methods

```py
driver.maximize_window()

input_field.send_keys('Devboi')

button.click()

input_field.submit()
```

# Automate finding Elements

## Name

```py
input_field = driver.find_element(By.NAME, 'demo-submission-name')
input_field.send_keys('Hello')
time.sleep(2)
input_field.submit() # submit input field
```

## Id

```py
input_field = driver.find_element(By.ID, 'demo-submission-id')
input_field.send_keys('Devboi')
time.sleep(2)
input_field.submit()
```

## Xpath

- Index counting is from 1

### Element

```py
# form_element = driver.find_element(By.XPATH, '/html/body/form[1]')
# form_element = driver.find_element(By.XPATH, '//form[1]') # /(html)/(body)
form_element = driver.find_element(By.XPATH, "//form[@id='demo-form']")
print(form_element.get_attribute('innerHTML'))

# ---------------------- PRINTS
# <label for="demo-submission">Make a test submission:</label>
# <input type="text" id="demo-submission-id" name="demo-submission-name">
# <input type="submit" value="Submit">
```

### Input

```py
# ----------------------------------------------- id or name
input_field = driver.find_element(By.XPATH, "//input[@name='q']")
input_field.send_keys('Omboi music')
input_field.submit()

# ---- could not get to work on Google but above does
# input_field = driver.find_element(By.XPATH, "//form[@role='search']/input[@name='q']")
#input_field.send_keys("Omboi music")
```

## CSS Selector

- Example

```py
# ------------------------------------- html tag & className tag.className
button = driver.find_element(By.CSS_SELECTOR, "a.gb_d")
button.click()
```

## Link text

- Example

```py
# ----------------------------------------- Text in link
link_text = driver.find_element(By.LINK_TEXT, "English")
link_text.click()
```

## Partial link text

- Example

```py
# ------------------- any amount of text in link text - must be element a(link)
partial_link_text = driver.find_element(By.PARTIAL_LINK_TEXT, "Zona")
partial_link_text.click()
```

## Class name

- Example

```py
# style-scope ytd-topbar-menu-button-renderer ------ class name of element
button = driver.find_element(By.CLASS_NAME, "style-scope ytd-topbar-menu-button-renderer")
button.click()
```

## Tag name

- Example

```py
# -------- will always return first element on page
button = driver.find_element(By.TAG_NAME, "button")
button.click()
```
