from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import requests
import re
import time
import os
import skype_credentials as credentials


class Login():

    def setup(self):

        try:
            email = credentials.USERNAME
            password = credentials.PASSWORD
            options = Options()
            options.headless = True
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--disable-extensions")
            options.add_argument("--proxy-server='direct://'")
            options.add_argument("--proxy-bypass-list=*")
            options.add_argument("--start-maximized")
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--no-sandbox')
            options.add_argument('--ignore-certificate-errors')
            screenshot_name = "screenshots/my_screenshot_name.png"
            self.driver = webdriver.Chrome(options=options)
            self.driver.get('https://login.live.com/login.srf')
            print("Headless Chrome Initialized")
            print("Page Title is : %s" % self.driver.title)
            element = self.driver.find_element_by_xpath(
                "//input[@class='form-control ltr_override' and @name='loginfmt']")
            element.click()
            element.clear()
            element.send_keys(email)
            self.driver.implicitly_wait(10)
            wait = WebDriverWait(self.driver, 60)
            waiting = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//input[@class='btn btn-block btn-primary' and @id='idSIButton9']")))
            signinelement = self.driver.find_element_by_xpath(
                "//input[@class='btn btn-block btn-primary' and @id='idSIButton9']")
            signinelement.click()
            print("Page Title is : %s" % self.driver.title)
            '''self.driver.find_element_by_xpath("//input[@class='btn btn-block btn-primary' and @id='idSIButton9']").click()'''

            self.driver.find_element_by_xpath(
                "//input[@name='passwd' and @type='password']").send_keys(password)

            wait = WebDriverWait(self.driver, 60)

            waiting = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//input[@class='btn btn-block btn-primary' and @type='submit']")))
            submitelement = self.driver.find_element_by_xpath(
                "//input[@class='btn btn-block btn-primary' and @type='submit']")
            submitelement.click()
            '''code for alert handling'''
            for i in range(0, 5):
                try:
                    click_alert = self.driver.switch_to.alert()
                    click_alert.dismiss()
                    continue
                except TimeoutException:
                    print('wrong value in'+i+'th row . Please check the value ')
                except NoAlertPresentException:
                    print('i = ', i, 'alert is not present yet, waiting for some time')
                    time.sleep(60)  # Delay for 1 minute (60 seconds)
                except Exception as e:
                    print("Unexpected error:", e)
                    raise
            ''' code for alert ends'''
            print("Page Title is : %s" % self.driver.title)

            '''self.driver.find_element_by_xpath("//input[@class='btn btn-block btn-primary' and @type='submit']").click()'''
            print("Page Title is : %s" % self.driver.title)
            self.driver.get("https://www.skype.com/en/")
            self.driver.implicitly_wait(60)
            print("Page Title is : %s" % self.driver.title)
            '''res = requests.get('https://www.skype.com/en/')'''
            '''res.raise_for_status()'''
            '''print(res.text)'''
            self.driver.implicitly_wait(10)
            wait = WebDriverWait(self.driver, 60)
            waiting = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//p[contains(@class, 'user-badge-email')]")))
            userlogin = self.driver.find_element_by_xpath(
                "//p[contains(@class, 'user-badge-email')]")
            time.sleep(1)
            print("User name is : %s" % userlogin.get_attribute('innerHTML'))
            source_code = userlogin.get_attribute('outerHTML')
            print("source code is: %s" % source_code)
            self.driver.implicitly_wait(30)
            self.driver.save_screenshot(screenshot_name)

        except Exception as e:

            print(e)

    def teardown(self):

        self.driver.quit()


if __name__ == "__main__":

    login = Login()
    login.setup()
