from time import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test_wework.base_page import BasePage


class ProfilePage(BasePage):

    _edit = (By.CSS_SELECTOR, ".qui_btn.ww_btn.js_edit")
    _username = (By.CSS_SELECTOR, "#username")
    _save = (By.CSS_SELECTOR, ".js_save")
    _success = (By.CSS_SELECTOR, ".success")
    _cancle = (By.CSS_SELECTOR, ".js_cancel")
    _disable = (By.CSS_SELECTOR, ".js_disable")

    def update(self, **kwargs):
        # 点击编辑
        self.click_by_js(*self._edit)
        element = self.driver.find_element(*self._username)
        element.clear()  # 清除名字
        element.send_keys(kwargs["name"])  # 更改名字
        self.click_by_js(*self._save)  # 点击保存
        # 等待 保存成功 提示出现
        tips = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(*self._success))
        assert tips.text == "保存成功"

    # 点击取消
    def cancle(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(*self._cancle))
        self.find(*self._cancle).click()

    # 点击禁用
    def diable(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(*self._disable))
        self.find(*self._disable).click()
        alert = self.driver.switch_to.alert
        alert.accept()
        assert "已禁用" in self.driver.page_source

    def enable(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(*self._disable))
        self.find(*self._disable).click()
        tips = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".success")))
        assert tips.text == "保存成功"

    def delete(self):
        pass

    def invite(self):
        pass