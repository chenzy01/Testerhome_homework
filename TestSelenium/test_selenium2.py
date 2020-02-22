import logging

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import pytest

logging.basicConfig(level=logging.INFO)


class Test_Selenium:

    def setup_method(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.debugger_address = "127.0.0.1:9222"  # 打开进程，开启一个调试开关
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('https://testerhome.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.quit()

    @pytest.mark.run(order=1)
    def test_scan_posts(self):  # 浏览帖子
        # 等待“查看更多”链接可见
        elem = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/topics/last"]')))
        elem.click()
        # self.driver.find_element_by_css_selector('.panel-heading>div>a[href="/topics/last"]').click()
        self.driver.execute_script('window.scrollBy(0,300)')  # 向下滚动
        self.driver.find_element_by_css_selector('[href="/topics/20036"]').click()  # 点击帖子
        sleep(1)

    @pytest.mark.run(order=2)
    def test_visit_shetuan(self):
        self.driver.find_element_by_css_selector('.nav.navbar-nav>li>a[href="/teams"]').click()
        sleep(1)
        self.driver.find_element_by_css_selector('[title="霍格沃兹测试学院(hogwarts)"]').click()
        sleep(1)
        # 选择第一个帖子
        self.driver.find_element_by_css_selector('.panel.topics>div.panel-body>div:nth-child(2) div.title>a').click()
        sleep(1)
        assert "访问被拒绝，你可能没有权限或未登录。" in self.driver.page_source

    @pytest.mark.run(order=3)
    def test_login(self):
        #self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element_by_css_selector('[href="/account/sign_in"]').click()
        sleep(1)
        element = self.driver.find_element_by_css_selector("#user_login")
        logging.info(element.is_displayed())
        logging.info(element.id)
        logging.info(element.tag_name)
        logging.info(element.text)
        logging.info(element.location)
        logging.info(element.size)
        logging.info(element.rect)
        logging.info(element.get_attribute("placeholder"))
        self.driver.find_element_by_css_selector("#user_login").send_keys("12345")  # 输入用户名
        self.driver.find_element_by_css_selector("#user_password").clear()
        self.driver.find_element_by_css_selector("#user_password").send_keys("12345")  # 输入密码
        self.driver.find_element_by_css_selector('[name = "commit"]').click()
        sleep(1)
        get_text = self.driver.find_element_by_css_selector('.alert.alert-warning').text
        # 账号/密码输入错误有三种提示
        assert get_text == "帐号或密码错误。" or "由于多次密码错误" in get_text or get_text == "Your account is locked."

    @pytest.mark.run(order=4)
    def test_testgirl(self):
        self.driver.find_element_by_css_selector('.form-group>input').send_keys("测试媛", keys.Keys.RETURN)
        sleep(2)
        # 查找测试媛成立的帖子
        self.driver.find_element_by_css_selector('.search-results>div.panel-body>div:nth-child(4) .topic.title>a').click()
        sleep(1)
        get_title = self.driver.title
        # # print(get_title)
        # 断言标题
        assert get_title == "TesterHome 测试媛组织成立啦"

    def test_upload(self):
        pass


if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', './report/xml'])