import os
import unittest
from unittest import TestCase
from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
class TestDemo(TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9'
        desired_caps['deviceName'] = 'Aqi'

        desired_caps['appPackage'] = 'com.jingdong.app.mall'
        desired_caps['appActivity'] = '.main.MainActivity'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test(self):
        self.driver.find_element_by_id('a4u').click()
        self.driver.find_element_by_id('search_text').send_keys('华为')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDemo)
    unittest.TextTestRunner(verbosity=2).run(suite)



