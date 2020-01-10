from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import re
import time
import skype_credentials as credentials


class Login():

    def setup(self):

        try:
            email = credentials.USERNAME
            password = credentials.PASSWORD
            my_window = {
                'width': 1920,
                'height': 1024
            }
            options = Options()
            options.headless = True
            options.add_argument("--headless")
            options.add_argument('--no-sandbox')
            options.add_argument("start-maximized")
            options.add_argument("disable-infobars")
            options.add_argument("--disable-extensions")
            options.add_argument('--ignore-certificate-errors')
            # or the login a href is not found and throws error
            options.add_argument(
                'window-size=' + str(my_window['width']) + 'x' + str(my_window['height']))
            self.driver = webdriver.Chrome(options=options)
            self.driver.implicitly_wait(30)
            self.driver.set_window_size(my_window['width'], my_window['height'])
            self.driver.get('https://www.skype.com/en/')
            print("Headless Chrome Initialized")
            print("Page Title is : %s" % self.driver.title)

            wait = WebDriverWait(self.driver, 10)
            '''linkelement = self.driver.find_element_by_xpath(
                "//a[@class='btn secondaryCta small usernameBtn notAuthenticated']")'''
            linkelement= self.driver.find_element_by_xpath("//a[contains(@class ,'usernameBtn notAuthenticated')]")
            ''''self.driver.execute_script("arguments[0].scrollIntoView();", linkelement)'''
            waiting = wait.until(EC.element_located_to_be_selected(
                (By.XPATH, "//a[@class='btn secondaryCta small usernameBtn notAuthenticated']")))
            '''linkelement = self.driver.find_element_by_xpath(
                "//a[@class='btn secondaryCta small usernameBtn notAuthenticated']").click()'''
            linkelement.click()
            print("Link accessed")

            wait = WebDriverWait(self.driver, 10)
            waiting = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//div[contains(@id, 'nav-buttons-wrapper')]//a[@role='menuitem' and contains(text(),'My account')]")))
            element = self.driver.find_element_by_xpath(
                "//div[contains(@id, 'nav-buttons-wrapper')]//a[@role='menuitem' and contains(text(),'My account')]").click()
            print("My account clicked")

            self.driver.implicitly_wait(10)
            userelement = self.driver.find_element_by_xpath(
                "//input[@class='form-control ltr_override' and @name='loginfmt']")
            print("Login form opened")

            userelement.click()
            userelement.clear()
            userelement.send_keys(email)
            print("Username entered")

            self.driver.find_element_by_xpath(
                "//input[@class='btn btn-block btn-primary' and @id='idSIButton9']").click()
            print("Next")

            self.driver.find_element_by_xpath(
                "//input[@name='passwd' and @type='password']").send_keys(password)
            print("Password entered")

            self.driver.implicitly_wait(10)
            wait = WebDriverWait(self.driver, 10)
            waiting = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//input[@class='btn btn-block btn-primary' and @type='submit']")))
            signinelement = self.driver.find_element_by_xpath(
                "//input[@class='btn btn-block btn-primary' and @type='submit']")
            signinelement.click()
            print("Page Title is : %s" % self.driver.title)

        except Exception as e:

            print(e)

    def teardown(self):

        self.driver.quit()


if __name__ == "__main__":

    login = Login()
    login.setup()
