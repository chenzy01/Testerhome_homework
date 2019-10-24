import logging

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_xueqiu_po_20190818.driver.app import App


class BasePage:

    def __init__(self):
        self.driver = App.driver

    # 查找元素
    def find(self, locator, value=None):
        if value is None:
            return self.driver.find_element(*locator)
        else:
            return self.driver.find_element(locator, value)

    # 显示等待定位单个元素
    def show_wait_find_element(self, locator, value=None):
        try:
            if value is None:
                return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(*locator))
            else:
                return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((locator, value)))
        except Exception as msg:
            return logging.info(msg)

    # 显示等待定位多个元素
    def show_wait_find_elements(self, locator, value=None):
        try:
            if value is None:
                return WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(*locator))
            else:
                return WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((locator, value)))
        except Exception as msg:
            return logging.info(msg)





