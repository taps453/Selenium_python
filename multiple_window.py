import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class multiple_window():
    def demo_driver(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()

        # Window Hanlde
        cur_win_handle = driver.current_window_handle
        print(cur_win_handle) 

        driver.find_element(By.XPATH, "//div[@id='themeSnipe']/section[@class='wrapper']/div[@class='right_data']/section[4]//div[@class='VueCarousel']//div[@class='VueCarousel-inner']/a[1]//img[@alt=' ']").click()
        all_handle = driver.window_handles
        print(all_handle)

        for handle in all_handle:
            if handle != cur_win_handle:
                driver.switch_to.window(handle)
                driver.find_element(By.ID, "BE_flight_origin_city").send_keys("New Delhi, India (DEL)")
                time.sleep(4)
                driver.close()
                time.sleep(2)
                break

        driver.switch_to.window(cur_win_handle)
        driver.find_element(By.XPATH,"//a[@id='booking_engine_hotels']/span[.='Hotels']").click()
        time.sleep(10)
        driver.quit()

demo = multiple_window()
demo.demo_driver()