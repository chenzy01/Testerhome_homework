from appium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class App:
    driver: WebDriver = None

    @classmethod
    def start(cls):
    # 初始化 driver
        caps = {"platformName": "Android",
                "deviceName": "android-emulator",
                "appPackage": "com.xueqiu.android",
                "appActivity": ".view.WelcomeActivityAlias",
                "autoGrantPermissions": "true"}
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(15)
        # return cls.driver



