from selenium.webdriver.common.by import By
import pytest
# hamcrest 一个 python 断言库
from hamcrest import *

from test_xueqiu_po_20190818.pages.xueqiu_page import XueqiuPage
from test_xueqiu_po_20190818.driver.app import App


class TestSearch:
    _user_profile = (By.ID, "user_profile_icon")
    _login_more = (By.ID, "login_more")
    _account = (By.ID, "login_account")
    _password = (By.ID, "login_password")
    _login_button = (By.ID, "button_next")
    _search = (By.ID, "com.xueqiu.android:id/home_search")  # 搜索框
    _search_input = (By.ID, "com.xueqiu.android:id/search_input_text")  # 搜索文本框
    _stock_name = (By.ID, "com.xueqiu.android:id/stockName")  # 股票/基金 名字
    _name_list = (By.ID, "com.xueqiu.android:id/name")  # 股票/基金 列表
    _cancle = (By.ID, "com.xueqiu.android:id/action_close")  # 取消

    def setup(self):
        self.xueqiu = XueqiuPage()


    def teardown(self):
        self.xueqiu.find(*self._cancle).click()

    # def teardown_class(self):
    #     sleep(2)
    #     self.driver.quit()

    def test_search_us(self):
        price = self.xueqiu.goto_search().search("alibaba").select(0).get_price("BABA")
        assert price > 100

    def test_search_us_other(self):
        assert "阿里" in self.xueqiu.goto_search().search("alibaba").select(-1).get_name()

    # def test_sendkeys(self):
    #     self.driver.keyevent(66)  # 键盘事件


if __name__ == '__main__':
    pytest.main()
