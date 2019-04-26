import logging
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from config.log.logger import *

class BaseView(object):
    def __init__(self,driver):
        self.driver = driver

    # def find_element(self, loc):
    #     element = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(loc))
    #     return element

    def find_Element(self, loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except NoSuchElementException:
            logging.error('Can not find element: %s' % loc[1])
            raise
        except TimeoutException:
            logging.error('Time out to find element: %s' % loc[1])
            raise

    def find_Elements(self,*loc):
        try:
            WebDriverWait(self.driver, 30).until(lambda driver: driver.find_elements(*loc))
            return self.driver.find_elements(*loc)
        except NoSuchElementException:
            logging.error('Can not find element: %s' % loc[1])
            raise
        except TimeoutException:
            logging.error('Time out to find element: %s' % loc[1])
            raise

    def click(self, loc):
        try:
            logging.info(('Click element by %s: %s' % (loc[0], loc[1])).encode('utf-8'))
            self.find_Element(loc).click()
        except AttributeError:
            raise

    def send_keys(self,loc,text):
        try:
            logging.info("Clear input-box:%s...." %loc[1])
            input=self.find_Element(loc).clear()
            logging.info("Input: %s" % text)
            input.send_keys(text)
        except AttributeError:
            raise

