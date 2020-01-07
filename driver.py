from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import re
import time
from selenium.webdriver.support.ui import WebDriverWait






class Login():

    def setup(self):

        try:
            self.driver=webdriver.Chrome()
            self.driver.delete_all_cookies()
            self.driver.get('https://web.skype.com/en/')
            self.driver.implicitly_wait(5)
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)
            is_displayed=self.driver.find_element_by_xpath(
                "//span[@class='title x-hidden-focus' and contains(text(),'Sign in')]").click()
            if is_displayed.is_displayed():
               print("Element displayed")
            result_flag=self.driver.find_element_by_xpath("//form[@id='i0281']")
            if result_flag.is_displayed():
               print("Moved to next tab")
            self.driver.switch_to_frame(result_flag)
            self.driver.find_element_by_id("i0116").send_keys("rahul.bhave81@outlook.com")
            self.driver.find_element_by_xpath("idSIButton9").click()

        except Exception as e:

            print(e)

    def teardown(self):

        self.driver.quit()
    
    



if __name__ == "__main__":

    login=Login()
    login.setup()
    login.teardown()
