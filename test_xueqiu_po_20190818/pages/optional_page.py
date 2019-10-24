from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from test_xueqiu_po_20190818.pages.base_page import BasePage
from test_xueqiu_po_20190818.pages.search_page import SearchPage


class OptionalPage(BasePage):
    _search = (By.ID, "com.xueqiu.android:id/home_search")  # 搜索框
    _search_circle = (By.ID, "com.xueqiu.android:id/action_search")  # 搜索按钮（圈）
    _search_input = (By.ID, "com.xueqiu.android:id/search_input_text")  # 搜索文本框
    _stock_name = (By.ID, "com.xueqiu.android:id/stockName")  # 股票/基金 名字
    _name_list = (By.ID, "com.xueqiu.android:id/name")  # 股票/基金 列表
    _cancle = (By.ID, "com.xueqiu.android:id/action_close")  # 取消
    _obtional_button = (By.XPATH, "//*[contains(@resource-id, 'tab_name') and @text='自选']")
    _follow_btn = (By.ID, "com.xueqiu.android:id/follow_btn")  # “加自选”按钮
    _followed_btn = (By.ID, "com.xueqiu.android:id/followed_btn")  # “已添加”按钮

    def search_stock(self):
        self.find(*self._search_circle).click()
        return SearchPage()

    def click_follow(self):
        """
        点击“加自选”
        :return:
        """
        self.show_wait_find_element(*self._follow_btn)
        self.find(*self._follow_btn).click()

    def click_followed(self):
        """
        点击“已自选”
        :return:
        """
        self.show_wait_find_element(*self._followed_btn)
        self.find(*self._followed_btn).click()

    def get_added_text(self):
        self.show_wait_find_element(*self._followed_btn)
        return self.find(*self._followed_btn).text

    def get_add_text(self):
        self.show_wait_find_element(*self._follow_btn)
        return self.find(*self._follow_btn).text

    def delete_optional(self, stock_name):
        ele = self.driver.find_element(By.XPATH, "//*[contains(@resource-id, 'portfolio_stockName') and @text='" +
                                       stock_name + "']")
        if ele:
            TouchAction(self.driver).long_press(el=ele, duration=3000).release().perform()  # 长按
            self.driver.find_element(By.XPATH, "//*[@text='删除']").click()

    def click_cancle(self):
        """
        点击取消按钮
        :return:
        """
        self.find(*self._cancle).click()
