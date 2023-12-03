import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class sliders:
    def slide(self):
        driver = webdriver.Chrome()
        driver.get("https://www.snapdeal.com/products/electronics-headphones?sort=plrty")
        driver.maximize_window()
        ele1 = driver.find_element(By.XPATH,"//a[contains(@class,'left-handle')]")
        ele2 = driver.find_element(By.XPATH,"//a[contains(@class,'right-handle')]")
        
    # 1st method
        # ActionChains(driver).drag_and_drop_by_offset(ele1, 60, 0).perform()
        # time.sleep(5)
        # ActionChains(driver).drag_and_drop_by_offset(ele2, -60, 0).perform()
        # time.sleep(5)
    # 2nd method
        # ActionChains(driver).click_and_hold(ele1).pause(1).move_by_offset(50,0).release().perform()
    #3rd method
        # ActionChains(driver).move_to_element(ele1).pause(1).click_and_hold(ele1).move_by_offset(80, 0).release().perform()
        driver.close()

obj = sliders()
obj.slide()

# ndJi5d snByac