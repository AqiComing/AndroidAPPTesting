from selenium.webdriver.common import keys

from baseview.base_view import BaseView
from appium.webdriver.common.mobileby import By


class JDMainPage(BaseView):
    close_ad_button=(By.ID,'com.jingdong.app.mall:id/bi_')
    search_textbox=(By.ID,'com.jingdong.app.mall:id/rv')

    def close_ad(self):
        self.click(self.close_ad_button)
    def click_search_box(self):
        self.click(self.search_textbox)
    # def search(self,text):
    #     self.send_keys(self.search_textbox,text)
