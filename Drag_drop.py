import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class drag_drop:
    def drop_drag(self):
        driver = webdriver.Chrome()
        driver.get("")
        driver.maximize_window()
        locator1 =""
        locator2 =""
        # method 1
        # ActionChains(driver).drag_and_drop('locator1','locator2').perform()
        
        # method 2
        ActionChains(driver).drag_and_drop_by_offset(locator1, x-corr,y-corr).perform()
        time.sleep()
        driver.close()

obj = drag_drop()
obj.drop_drag()