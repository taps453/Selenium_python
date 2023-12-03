import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class iframe:
    def demo_iframe(self):
        driver = webdriver.Chrome()
        driver.get("")
        driver.maximize_window()
        driver.find_element(By.ID,"")

        #switch with locator
        #switch with ID
        #switch with name
        #switch with Index