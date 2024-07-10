from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# Find by css:
driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")

# Find by css but using classes:
driver.find_element(By.CSS_SELECTOR, ".nav-input")
driver.find_element(By.CSS_SELECTOR, ".nav-input.nav-progressive-attribute")

# Find by tags and classes:
driver.find_element(By.CSS_SELECTOR, "input.nav-input.nav-progressive-attribute")

# Find by tag + id + classes
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox.nav-input.nav-progressive-attribute")

# Attributes
driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon']")
driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon'][type='text']")

# Tag + Attributes
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search Amazon'][type='text']")

# Tag + #id + .class + [attributes]
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox.nav-input[placeholder='Search Amazon'][type='text']")

# Attributes, partial match
driver.find_element(By.CSS_SELECTOR, "[placeholder*='Search Ama']")
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_signin_notification_privacy_notice']")
driver.find_element(By.CSS_SELECTOR, "a[class*='ap_signin_notification_privacy_notice']")

# Multiple notes, parent => child
driver.find_element(By.CSS_SELECTOR, "div.a-box div#LegalTextRow a[href*='condition']")

