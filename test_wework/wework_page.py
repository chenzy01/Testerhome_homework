from selenium import webdriver


class WeWork:
    def __init__(self):
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
            # "wwrtx.vst": "aEF8NdIm3Lgp8zDThc6ubpkLrWmHcoHQKIiaUr3IkGEfU9H0QRQOzFPF5l8IlXxvsWu5v3ugnkaXGAZS4adiusJSzwSxMt02cIUm96_KLGq07hEe21F5MKNp8WhfQZ54a_kEePYdD3aJ9O89v35HLqb2Kgs_OPYO8923R9f-ouKVRcU5N2kpduvKhAA4dEnRRhliq4_i2X7Bt_M_tQq8LH9MpITl7HLuljrTagMU0RJtHgvpyjwP7aZbCgGzLs-ZEzSaDzEOkmqx67PlXvq2WA",
            # "wwrtx.d2st": "a662250",
            "wwrtx.sid": "7zhvco-IuYlN-opFGfDBIZJWfyTNd9pbtBd8d5RUuNuIcJsg-edD77-sxR0FuebI",
            # "wwrtx.ltype": "1",
            # "wxpay.corpid": "1970325062080397",
            # "wxpay.vid": "1688853366461865",
            # "wwrtx.vid": "1688853366461865",
            # "wwrtx.logined": "true",
        }
        for k, v in cookies.items():
            self.driver.add_cookie({"name": k, "value": v})
        self.driver.get(url)  # 上面设置好cookies，然后登录（绕过了扫码）

    def quit(self):
        self.driver.quit()