import os
import sys

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from baseview.base_view import BaseView

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

class InitPage(BaseView):
    iknow_button=(By.ID,'bnm')
    sure_button=(By.ID,'android:id/button1')

    def goto_mainpage(self):
        self.click(self.iknow_button)
        self.click(self.sure_button)



