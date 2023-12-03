import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Implicit_waits():
    def wait(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.yatra.com/")
        
        # wait = WebDriverWait(driver, 10)
        # element = wait.until(
        #     EC.element_to_be_clickable((By.ID, "exampleID")))

        # element = wait.until(
        #         EC.visibility_of_element_located((By.XPATH, "//div[@id='example']")))

obj = Implicit_waits()
obj.wait()

