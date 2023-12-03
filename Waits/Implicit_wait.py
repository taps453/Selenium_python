'''
IMPLICIT WAIT - 
1- Implicit wait tells the webdriver maximum wait time when searching for
   elements before throwing exception.
2- Implicit wait is global , it is applicable to all the webelements in the
   script.

Explicit wait - 
1- Explicit waits tell the webdriver to halt the execution until a particular
   condition is met or maximum wait time has passed.
2- It's applicable only to  those webelements which are specified by the user.

Fluent wait - 
1- Fluent Wait is a type of explicit wait in Selenium that provides more 
flexibility and allows you to define the polling frequency as well as to 
ignore specific types of exceptions during the waiting period.

poll_frequency is the frequency with which WebDriver should check the 
expected condition.
'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class waits():
    def wait(self):
        driver = webdriver.Chrome()
        driver.maximize_window()

        # Implicit wait 

        driver.implicitly_wait(10)
        driver.get("https://login.salesforce.com/?locale=in")
        driver.find_element(By.ID,"username").send_keys("ab@gmail.com")
       
       # Fluent wait
        driver.close()


obj = waits()
obj.wait()