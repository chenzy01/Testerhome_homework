from appium import webdriver
from selenium.webdriver.common.by import By

from test_xueqiu_po_20190818.pages.base_page import BasePage
from test_xueqiu_po_20190818.pages.optional_page import OptionalPage
from test_xueqiu_po_20190818.pages.profile_page import ProfilePage
from test_xueqiu_po_20190818.pages.search_page import SearchPage
from test_xueqiu_po_20190818.driver.app import App


class XueqiuPage(BasePage):
    _tag_name = (By.XPATH, "//*[contains(@resource-id, 'tab_name') and @text='自选']")

    # def start_app(self):
    #     App.start()

    def goto_search(self):
        self.find(By.ID, "home_search").click()
        return SearchPage()

    def goto_profile(self):
        return ProfilePage()

    def goto_optional(self):
        self.find(self._tag_name).click()
        return OptionalPage()

    def get_ads(self):
        return True
