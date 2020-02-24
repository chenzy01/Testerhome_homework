# coding:utf-8

import logging
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import pytest
from selenium.webdriver.support.ui import Select

logging.basicConfig(level=logging.INFO)


class Test_Wework:

    def setup_method(self):
        """
        在调试模式下：
        1、chrome要提前关闭所有进程
        2、在CMD中执行命令“chrome.exe --remote-debugging-port=9222”，注意chrome.exe是否加到环境
        变量中，没有则用绝对路径表示
        3、上面执行完成后，再执行下面程序
        """
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.debugger_address = "127.0.0.1:9222"  # 打开进程，开启一个调试开关
        # self.driver = webdriver.Chrome(options=chrome_options)
        # self.driver.get('https://testerhome.com/')

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        url = "https://work.weixin.qq.com/wework_admin/frame"
        self.driver.get(url)  # 跳到企业微信登录界面
        # 设置新增的cookies
        cookies = {
            "wwrtx.vst": "3482fw8k4-pdHc7UoNpwq8Jm0mi3Xxfl-Lp2d-B02JF4P81I-UI-lywHIOzVYc1EZRJ2oX9KRvYPFfnX_1BvYm8VbK5OBYHFlT8EcZdrAJh-lqrcGK61XX-JeZmtmOj1KcC5k2_HZh45SuWjPRIcMrPJz1K86plRgrjIR3e6dVBUoW7toiSsK0N0pTGMKsKFGivkOg0ApxMAsDrXkuIanMJSHQK_vN8tJrXpWEF5n9ps-8UweI_C_KXDqX7yNWIivC6CPLw-YgK3mVrp7jf-bA",
            "wwrtx.d2st": "a4347562",
            "wwrtx.sid": "7zhvco-IuYlN-opFGfDBIX23EYDCdmX34YrV1QjX0fbIurlh-uUXCzxW8bHSJSwL",
            "wwrtx.ltype": "1",
            "wxpay.corpid": "1970325062080397",
            "wxpay.vid": "1688853366461865",
            "wwrtx.vid": "1688853366461865",
            "wwrtx.logined": "true",
        }
        for k, v in cookies.items():
            self.driver.add_cookie({"name": k, "value": v})
        self.driver.get(url)  # 上面设置好cookies，然后登录（绕过了扫码）

    def teardown_method(self):
        pass
        # sleep(3)
        # self.driver.quit()

    def click_by_js(self, by, locator):
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(by, locator))

    def test_login(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        # self.driver.find_element_by_css_selector('[href="/account/sign_in"]').click()
        # element = self.driver.find_element_by_css_selector("#user_login")
        # logging.info(element.is_displayed())
        # logging.info(element.id)
        # logging.info(element.tag_name)
        # logging.info(element.text)
        # logging.info(element.location)
        # logging.info(element.size)
        # logging.info(element.rect)
        # logging.info(element.get_attribute("placeholder"))
        self.driver.find_element_by_css_selector("#user_login").clear()
        self.driver.find_element_by_css_selector("#user_login").send_keys("12345")  # 输入用户名
        self.driver.find_element_by_css_selector("#user_password").clear()
        self.driver.find_element_by_css_selector("#user_password").send_keys("12345")  # 输入密码
        self.driver.find_element_by_css_selector('[name = "commit"]').click()
        self.driver.find_element(By.CSS_SELECTOR, "#user_remember_me").click()
        self.driver.find_element(By.NAME, "commit").click()
        sleep(5)

    # 上传图像
    def test_upload_images(self):
        element_add = self.driver.find_element(By.CSS_SELECTOR, ".js_upload_file_selector")
        # element_add.click()
        # print(self.driver.execute_script("console.log('hello from selenium')"))
        # print(self.driver.execute_script("return document.title;"))
        self.driver.execute_script("arguments[0].click();", element_add)  # 使用js方法进行点击
        # 通过 send_keys()方法上传图片,注意路径要使用反斜杠
        self.driver.find_element(By.CSS_SELECTOR, ".material_upload_input").\
            send_keys("C:/Users/CZY/PycharmProjects/Demo/images/起风了.jpg")
        # material_picCard_cnt_cancelBtn js_uploadProgress_cancel
        WebDriverWait(self.driver, 15).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".js_uploadProgress_cancel")))
        self.driver.find_element(By.CSS_SELECTOR, ".js_next").click()
        sleep(5)

    # 添加成员
    def test_add_member(self):
        self.driver.find_element(By.CSS_SELECTOR, "#menu_contacts").click()  # 点击通讯录菜单
        # 点击添加成员
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".js_has_member a.qui_btn.ww_btn.js_add_member")))
        self.click_by_js(By.CSS_SELECTOR, ".js_add_member")
        # ele = self.driver.find_element(By.CSS_SELECTOR, ".js_has_member a.qui_btn.ww_btn.js_add_member")
        # ele.click()
        # 姓名
        self.driver.find_element(By.CSS_SELECTOR, "#username").send_keys("tester")
        # 账号
        self.driver.find_element(By.CSS_SELECTOR, "#memberAdd_acctid").send_keys("tester001")
        # 手机号
        self.driver.find_element(By.CSS_SELECTOR, ".ww_telInput_mainNumber").send_keys("13800138001")
        # 邮箱
        self.driver.find_element(By.CSS_SELECTOR, "#memberAdd_mail").send_keys("123@qq.com")
        # # 保存
        # self.driver.find_element(By.CSS_SELECTOR, ".member_colRight_operationBar .js_btn_save").click()
        # tips = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".success")))
        # assert tips.text == "保存成功"
        # assert "保存成功" in self.driver.page_source

    def test_cookie(self):
        pass
        # url = "https://work.weixin.qq.com/wework_admin/frame"
        # self.driver.get(url)
        # cookies = {
        #     "wwrtx.vst": "3482fw8k4-pdHc7UoNpwq8Jm0mi3Xxfl-Lp2d-B02JF4P81I-UI-lywHIOzVYc1EZRJ2oX9KRvYPFfnX_1BvYm8VbK5OBYHFlT8EcZdrAJh-lqrcGK61XX-JeZmtmOj1KcC5k2_HZh45SuWjPRIcMrPJz1K86plRgrjIR3e6dVBUoW7toiSsK0N0pTGMKsKFGivkOg0ApxMAsDrXkuIanMJSHQK_vN8tJrXpWEF5n9ps-8UweI_C_KXDqX7yNWIivC6CPLw-YgK3mVrp7jf-bA",
        #     "wwrtx.d2st": "a4347562",
        #     "wwrtx.sid": "7zhvco-IuYlN-opFGfDBIX23EYDCdmX34YrV1QjX0fbIurlh-uUXCzxW8bHSJSwL",
        #     "wwrtx.ltype": "1",
        #     "wxpay.corpid": "1970325062080397",
        #     "wxpay.vid": "1688853366461865",
        #     "wwrtx.vid": "1688853366461865",
        #     "wwrtx.logined": "true",
        # }
        # for k, v in cookies.items():
        #     self.driver.add_cookie({"name": k, "value": v})
        # self.driver.get(url)


if __name__ == '__main__':
    pytest.main()