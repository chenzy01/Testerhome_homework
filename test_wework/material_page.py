from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test_wework.base_page import BasePage


class MeterialPage(BasePage):
    _select_pic = (By.CSS_SELECTOR, "#ww_tabNav_item_Curr")
    _upload_pic = (By.CSS_SELECTOR, ".js_upload_file_selector")
    _complete = (By.CSS_SELECTOR, ".js_next")
    _cancle = (By.CSS_SELECTOR, ".js_uploadProgress_cancel")
    _list_total = (By.CSS_SELECTOR, ".js_list_total")

    # 上传图像
    def upload_images(self, path):
        # 选择图片
        self.find(*self._select_pic).click()
        # 点击添加图片,使用js方法进行点击
        self.click_by_js(*self._upload_pic)
        # 通过 send_keys()方法上传图片,注意路径要使用反斜杠
        self.find(By.CSS_SELECTOR, ".material_upload_input").send_keys(path)
        # material_picCard_cnt_cancelBtn js_uploadProgress_cancel
        WebDriverWait(self.driver, 15).until(EC.invisibility_of_element_located(*self._cancle))
        # 点击完成
        self.find(*self._complete).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of(*self._list_total))