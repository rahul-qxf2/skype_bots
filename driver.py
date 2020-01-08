from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import re
import time
import skype_credentials as credentials


class Login():

    def setup(self):

        try:
            email = credentials.USERNAME
            password = credentials.PASSWORD
            options = Options()
            options.add_argument("start-maximized")
            options.add_argument("disable-infobars")
            options.add_argument("--disable-extensions")
            self.driver = webdriver.Chrome(options=options)
            self.driver.get('https://www.skype.com/en/')
            print("Page Title is : %s" % self.driver.title)
            linkelement= self.driver.find_element_by_xpath(
                "//a[@class='btn secondaryCta small usernameBtn notAuthenticated']").click()
            element =self.driver.find_element_by_xpath(
                "//div[contains(@id, 'nav-buttons-wrapper')]//a[@role='menuitem' and contains(text(),'My account')]").click()
            self.driver.implicitly_wait(10)
            userelement =self.driver.find_element_by_xpath(
                "//input[@class='form-control ltr_override' and @name='loginfmt']")
            userelement.click()
            userelement.clear()
            userelement.send_keys(email)
            self.driver.find_element_by_xpath("//input[@class='btn btn-block btn-primary' and @id='idSIButton9']").click()
            self.driver.find_element_by_xpath("//input[@name='passwd' and @type='password']").send_keys(password)
            self.driver.implicitly_wait(10)
            wait= WebDriverWait(self.driver,10)
            waiting = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@class='btn btn-block btn-primary' and @type='submit']")))
            signinelement=self.driver.find_element_by_xpath("//input[@class='btn btn-block btn-primary' and @type='submit']")
            signinelement.click()
            print("Page Title is : %s" % self.driver.title)
           
            
            
         
        except Exception as e:

            print(e)

    
    def teardown(self):

        self.driver.quit()


if __name__ == "__main__":

    login = Login()
    login.setup()
