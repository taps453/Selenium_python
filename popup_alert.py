import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class popup_window():
    def pop_driver(self):
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
        driver.maximize_window()
        driver.switch_to.frame("iframeResult")
        #Accept laert
        driver.find_element(By.XPATH,"//button[normalize-space()='Try it']").click()
        time.sleep(4)
        driver.switch_to.alert.accept()
        time.sleep(4)

        #Dismiss alert
        driver.find_element(By.XPATH,"//button[normalize-space()='Try it']").click()
        time.sleep(4)
        driver.switch_to.alert.dismiss()
        time.sleep(4)# use waits

        # enter value in popup alert and then click enter
        #driver.switch_to.alert.send_keys(" -- ")
        #driver.switch_to.alert.accept()


obj = popup_window()
obj.pop_driver()