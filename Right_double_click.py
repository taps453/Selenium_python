import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class double_right_click():
    def right_click(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("http://demo.guru99.com/test/simple_context_menu.html")

        # # Right click
        # achain = ActionChains(driver)
        # ele1 = driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
        # achain.context_click(ele1).perform()
        # time.sleep(4)
        # driver.find_element(By.XPATH,"//span[normalize-space()='Copy']").click()
        # time .sleep(4)
        # driver.close()

        #Double click
        achain =ActionChains(driver)
        ele2 = driver.find_element(By.XPATH,"//button[normalize-space()='Double-Click Me To See Alert']")
        achain.double_click(ele2).perform()
        time.sleep(4)
        driver.close()

obj = double_right_click()
obj.right_click()

#