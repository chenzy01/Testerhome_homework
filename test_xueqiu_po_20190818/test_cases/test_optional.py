from time import sleep

from test_xueqiu_po_20190818.driver.app import App
from test_xueqiu_po_20190818.pages.optional_page import OptionalPage
from test_xueqiu_po_20190818.pages.search_page import SearchPage
from test_xueqiu_po_20190818.pages.xueqiu_page import XueqiuPage


class TestOptional:

    @classmethod
    def setup_class(cls):
        App.start()

    def setup(self):
        self.xueqiu = XueqiuPage()
        self.optional = OptionalPage()
        self.searchpage = SearchPage()

    def teardown(self):
        sleep(1)
        App.driver.quit()

    def test_add_optional(self):
        self.xueqiu.goto_optional()  # 点击“自选”
        self.optional.search_stock().search("xiaomi").select(0)  # 搜索小米
        self.optional.click_follow()
        self.searchpage.click_cancle()
        self.optional.search_stock().search("xiaomi").select(0)
        assert "已添加" == self.optional.get_added_text()

    def test_delete_optional_1(self):
        self.xueqiu.goto_optional()
        self.optional.search_stock().search("xiaomi").select(0)
        optional_text = self.optional.get_added_text()
        if optional_text == "已添加":
            self.optional.click_followed()  # 点击“已自选”进行删除
            self.searchpage.click_cancle()
            self.optional.search_stock().search("xiaomi").select(0)
            assert "加自选" == self.optional.get_add_text()
        elif optional_text == "加自选":
            pass

    def test_delete_optional_2(self):
        self.xueqiu.goto_optional()
        self.optional.delete_optional("小米集团-W")  # 删除已选股票
        self.optional.search_stock().search("xiaomi").select(0)
        self.optional.click_follow()
        optional_text = self.optional.get_added_text()
        assert optional_text == "已添加"
















