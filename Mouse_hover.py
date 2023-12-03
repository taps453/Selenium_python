import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class Mouse_hover():
    def hover_mouse(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        
        button_hover = driver.find_element(By.CLASS_NAME,"more-arr")
        
        act_chain = ActionChains(driver)
        act_chain.move_to_element(button_hover).perform()
        
        driver.find_element(By.XPATH,"//a[@id='booking_engine_monument']/span[.='Monuments']").click()
        time.sleep(10)
        driver.quit()

obj = Mouse_hover()
obj.hover_mouse()
