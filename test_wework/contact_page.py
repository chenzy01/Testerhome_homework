from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test_wework.base_page import BasePage
from test_wework.profile_page import ProfilePage


class ContactPage(BasePage):
    _contacts = (By.CSS_SELECTOR, "#menu_contacts")
    _username = (By.CSS_SELECTOR, "#username")
    _alias = (By.CSS_SELECTOR, "#memberAdd_english_name")
    _id = (By.CSS_SELECTOR, "#memberAdd_acctid")
    _mobile = (By.CSS_SELECTOR, ".ww_telInput_mainNumber")
    _mail = (By.CSS_SELECTOR, "#memberAdd_mail")
    _save = (By.CSS_SELECTOR, ".member_colRight_operationBar .js_btn_save")
    _search = (By.CSS_SELECTOR, ".ww_searchInput_text")
    _add = (By.CSS_SELECTOR, ".js_has_member a.qui_btn.ww_btn.js_add_member")

    def __init__(self, wework, driver: WebDriver):
        super().__init__(driver)
        self.driver = wework.driver

    def add_member(self, name, alias, id, mobile, **kwargs):
        self.driver.find_element(*self._contacts).click()  # 点击通讯录菜单
        # 点击添加成员
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(*self._add))
        self.click_by_js(*self._add)
        # 姓名
        self.find(*self._username).send_keys(name)  # 此时加*和不加*都可以，*表示把改参数拆成了两部分
        # 别名
        self.find(*self._alias).send_keys(alias)
        # 账号
        self.find(*self._id).send_keys(id)
        # 手机号
        self.driver.find_element(*self._mobile).send_keys(mobile)
        # 邮箱
        self.driver.find_element(*self._mail).send_keys("123@qq.com")
        # 保存
        self.driver.find_element(*self._save).click()
        tips = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".success")))
        assert tips.text == "保存成功"
        # assert "保存成功" in self.driver.page_source

    def delete_member(self):
        pass

    def search(self, key):
        self.driver.find_element(*self._contacts).click()  # 点击通讯录菜单
        # 在通讯录下，向搜索框赋值
        self.find(self._search).send_keys(key)
        return ProfilePage(self.driver)