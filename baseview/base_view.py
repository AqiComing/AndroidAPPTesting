from pip._internal.utils import logging
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

class BaseView(object):
    def __init__(self,driver):
        self.driver = driver

    def find_Element(self,loc):
        try:
            element = WebDriverWait(self.driver, 30).until(lambda driver:driver.find_element(*loc).is_displayed())
            return element
        except NoSuchElementException:
            logging.error('Can not find element: %s' % loc[1])
            raise
        except TimeoutException:
            logging.error('Time out to find element: %s' % loc[1])
            raise

    def click(self, loc):
        try:
            ele = self.find_Element(loc)
            logging.info(('Click element by %s: %s' % (loc[0], loc[1])).encode('utf-8'))
            ele.click()
        except AttributeError:
            raise
