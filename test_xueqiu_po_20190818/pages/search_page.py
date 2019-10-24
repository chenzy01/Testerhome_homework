from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from test_xueqiu_po_20190818.driver.app import App
from test_xueqiu_po_20190818.pages.base_page import BasePage


class SearchPage(BasePage):
    _search = (By.ID, "com.xueqiu.android:id/home_search")  # 搜索框
    _search_input = (By.ID, "com.xueqiu.android:id/search_input_text")  # 搜索文本框
    _stock_name = (By.ID, "com.xueqiu.android:id/stockName")  # 股票/基金 名字
    _cancle = (By.ID, "com.xueqiu.android:id/action_close")  # 取消
    _obtional_button = (By.XPATH, "//*[contains(@id, 'tab_icon') and @text='自选']")
    _follow_btn = (By.ID, "com.xueqiu.android:id/follow_btn")  # “加自选”按钮

    def search(self, keyword):
        self.find(By.ID, "search_input_text").click()
        self.find(By.ID, "search_input_text").send_keys(keyword)
        return self

    def select(self, index):
        self.show_wait_find_elements(By.ID, "com.xueqiu.android:id/name")
        self.driver.find_elements(By.ID, "com.xueqiu.android:id/name")[index].click()
        return self

    def get_name(self):
        return self.driver.page_source

    def get_price(self, stock_type):
        price = self.driver.find_element_by_xpath(
            "//*[contains(@resource-id, 'stockCode') and @text='" + stock_type + "']/../../.."
            "//*[contains(@resource-id, 'current_price')]").text
        price = float(price)
        return price

    def click_cancle(self):
        """
        点击取消按钮
        :return:
        """
        self.find(self._cancle).click()
        return self


