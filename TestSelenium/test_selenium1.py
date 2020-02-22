from selenium import webdriver
from time import sleep
import pytest


class Test_Selenium:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://testerhome.com/')
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def test_testhome(self):
        # 点击文章《图像分类、AI 与全自动性能测试》
        self.driver.find_element_by_css_selector('[href="/topics/19978"]').click()
        sleep(1)
        self.driver.find_element_by_css_selector(".fa.fa-list").click()  # 点击目录按钮
        sleep(2)
        # 点击“应用举例”子目录
        self.driver.find_element_by_css_selector("div.list-container>ul>li:nth-child(4)").click()
        sleep(3)

    def teardown_method(self):
        self.driver.quit()


if __name__ == '__main__':
    pytest.main()
