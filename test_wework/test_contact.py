from time import sleep, time

from selenium import webdriver

from test_wework.contact_page import ContactPage
from test_wework.wework_page import WeWork


class TestContact:

    def setup(self):
        self.work = WeWork()
        self.contact = ContactPage(self.work.driver)

    def teardown(self):
        pass
        # sleep(3)
        # self.work.quit()

    def test_add_member(self):
        self.contact.add_member("seveniruby", "seveniruby", "seveniruby", "15809099890")
        assert self.contact.get_tips() == "OK"

    def test_add_member_chinese(self):
        self.contact.add_member("哈哈", "哈哈", "seveniruby_1", "15809099891")
        assert self.contact.get_tips() == "OK"

    def test_delete(self):
        udid = str(time())  # 加上这个标识，可设置唯一值
        self.contact.add_member("哈哈"+udid, "哈哈"+udid, "seveniruby_1"+udid, "15809099892")

    def test_update_profile(self):
        self.contact.search("tester001").update(name="tester %s" % str(time()))






