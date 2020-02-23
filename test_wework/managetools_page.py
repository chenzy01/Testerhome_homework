from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from test_wework.base_page import BasePage
from test_wework.material_page import MeterialPage


class ManageToolsPage(BasePage):
    # def __init__(self, wework, driver: WebDriver):
    #     super().__init__(driver)
    #     self.driver = wework.driver

    def choose_tool(self, tool):
        # self.tool = tool
        if tool == "成员加入":
            self.find(By.LINK_TEXT, "成员加入").click()
        elif tool == "通讯录同步":
            self.find(By.LINK_TEXT, "通讯录同步").click()
        elif tool == "消息群发":
            self.find(By.LINK_TEXT, "消息群发").click()
        elif tool == "用户消息":
            self.find(By.LINK_TEXT, "用户消息").click()
        elif tool == "素材库":
            self.find(By.LINK_TEXT, "素材库").click()
            return MeterialPage(self.driver)
        elif tool == "员工服务":
            self.find(By.LINK_TEXT, "员工服务").click()
        elif tool == "使用分析":
            self.find(By.LINK_TEXT, "使用分析").click()
        elif tool == "奖励":
            self.find(By.LINK_TEXT, "奖励").click()
        elif tool == "一周小结":
            self.find(By.LINK_TEXT, "一周小结").click()















