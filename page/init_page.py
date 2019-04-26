import os
import sys
from appium.webdriver.common.mobileby import By

from baseview.base_view import BaseView

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

class InitPage(BaseView):
    iknow_button=(By.ID,'com.jingdong.app.mall:id/bpi')
    start_buttin=(By.ID,'com.jingdong.app.mall:id/c4x')
    skip_button=(By.ID,'com.jingdong.app.mall:id/apw')
    sure_button=(By.ID,'android:id/button1')

    def goto_mainpage(self):
        self.click(self.iknow_button)
        self.click(self.start_buttin)
        self.click(self.skip_button)
        self.click(self.sure_button)



