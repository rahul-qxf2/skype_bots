import unittest
import skype_credentials as credentials
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from importlib import reload
from selenium import webdriver
from xvfbwrapper import Xvfb
import re
import time


class TestPages(unittest.TestCase):

    def setUp(self):
        self.xvfb = Xvfb(width=1280, height=720)
        self.addCleanup(self.xvfb.stop)
        self.xvfb.start()
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def testUbuntuHomepage(self):
        self.browser.get('http://www.ubuntu.com')
        self.assertIn('Ubuntu', self.browser.title)

    def testGoogleHomepage(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)
    
    def LoginSkype(self):
        try:
            email = credentials.USERNAME
            password = credentials.PASSWORD
            self.browser.get('https://www.skype.com/en/')
            print("Headless Browser Initialized")
            print("Page Title is : %s" % self.browser.title)
            wait = WebDriverWait(self.browser, 10)
            linkelement = self.browser.find_element_by_xpath(
                "//a[@class='btn secondaryCta small usernameBtn notAuthenticated']")
            ''''self.driver.execute_script("arguments[0].scrollIntoView();", linkelement)'''
            waiting = wait.until(EC.element_located_to_be_selected(
                (By.XPATH, "//a[@class='btn secondaryCta small usernameBtn notAuthenticated']")))
            '''linkelement = self.driver.find_element_by_xpath(
                "//a[@class='btn secondaryCta small usernameBtn notAuthenticated']").click()'''
            linkelement.click()
            print("Link accessed")

            wait = WebDriverWait(self.browser, 10)
            waiting = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//div[contains(@id, 'nav-buttons-wrapper')]//a[@role='menuitem' and contains(text(),'My account')]")))
            element = self.browser.find_element_by_xpath(
                "//div[contains(@id, 'nav-buttons-wrapper')]//a[@role='menuitem' and contains(text(),'My account')]").click()
            print("My account clicked")

            self.browser.implicitly_wait(10)
            userelement = self.browser.find_element_by_xpath(
                "//input[@class='form-control ltr_override' and @name='loginfmt']")
            print("Login form opened")

            userelement.click()
            userelement.clear()
            userelement.send_keys(email)
            print("Username entered")

            self.browser.find_element_by_xpath(
                "//input[@class='btn btn-block btn-primary' and @id='idSIButton9']").click()
            print("Next")

            self.browser.find_element_by_xpath(
                "//input[@name='passwd' and @type='password']").send_keys(password)
            print("Password entered")

            self.browser.implicitly_wait(10)
            wait = WebDriverWait(self.browser, 10)
            waiting = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//input[@class='btn btn-block btn-primary' and @type='submit']")))
            signinelement = self.browser.find_element_by_xpath(
                "//input[@class='btn btn-block btn-primary' and @type='submit']")
            signinelement.click()
            print("Page Title is : %s" % self.browser.title)

        except Exception as e:

            print(e)



if __name__ == '__main__':
    unittest.main()