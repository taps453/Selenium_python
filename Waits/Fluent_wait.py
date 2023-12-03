from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import FluentWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Set up the WebDriver
driver = webdriver.Chrome()

# Define a Fluent Wait with a timeout of 30 seconds, polling every 5 seconds
wait = WebDriverWait(driver, timeout=30, poll_frequency=5, ignored_exceptions=[TimeoutException])

# Use Fluent Wait to wait for a certain condition (e.g., presence of an element)
element = wait.until(EC.presence_of_element_located((By.ID, "exampleID")))
element.click()
driver.quit()
