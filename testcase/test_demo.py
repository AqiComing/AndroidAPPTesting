import os
import sys
import unittest
from unittest import TestCase
from common.test_caps import caps
from appium import webdriver

# Returns abs path relative to this file and not cwd
from page.init_page import InitPage
from page.jd_main_page import JDMainPage

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class TestDemo(TestCase):
    def setUp(self):
        self.driver = caps()
        initPage = InitPage(self.driver)
        initPage.goto_mainpage()

        jdMainPage=JDMainPage(self.driver)
        jdMainPage.close_ad()
        jdMainPage.search('华为')

    def tearDown(self):
        self.driver.quit()

    def test(self):

        self.driver.find_element_by_id('bnm').click()
        self.driver.find_element_by_id('android:id/button1').click()
        self.driver.find_element_by_id('search_text').send_keys('华为')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDemo)
    unittest.TextTestRunner(verbosity=2).run(suite)




