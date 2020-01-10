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
            self.driver = webdriver.Chrome(chrome_options=options)
            self.driver.get('https://login.live.com/login.srf')
            print("Page Title is : %s" % self.driver.title)
            element =self.driver.find_element_by_xpath(
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

            self.driver.find_element_by_xpath("//input[@name='passwd' and @type='password']").send_keys(password)
            self.driver.find_element_by_xpath("//input[@class='btn btn-block btn-primary' and @type='submit']").click()
            print("Page Title is : %s" % self.driver.title)
        except Exception as e:

            print(e)

    def teardown(self):

        self.driver.quit()


if __name__ == "__main__":

    login = Login()
    login.setup()
