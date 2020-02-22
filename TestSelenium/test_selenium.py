from selenium import webdriver
from time import sleep
import pytest


class Test_Selenium:

    def setup_method(self):
        self.bro = webdriver.Chrome()

    def test_testhome(self):
        self.bro.get('https://testerhome.com/')
        self.bro.implicitly_wait(5)
        self.bro.maximize_window()
        sleep(1)
        self.bro.find_element_by_link_text("先到先得！第五届中国移动互联网测试开发大会 PPT 提供下载啦").click()
        sleep(1)
        self.bro.find_element_by_link_text("https://testerhome.com/topics/19664").click()
        self.bro.implicitly_wait(5)
        handles = self.bro.window_handles
        self.bro.switch_to.window(handles[-1])
        sleep(1)
        assert "有奖投票" in self.bro.page_source

    def teardown_method(self):
        self.bro.quit()


if __name__ == '__main__':
    pytest.main()