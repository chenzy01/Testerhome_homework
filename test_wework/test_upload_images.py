from test_wework.material_page import MeterialPage
from test_wework.wework_page import WeWork
from test_wework.managetools_page import ManageToolsPage


class TestUploadImages:

    def setUp(self):
        self.work = WeWork()
        self.upload = MeterialPage(self.work.driver)
        self.choose_tool = ManageToolsPage(self.work.driver)

    def teardown(self):
        pass
        # sleep(3)
        # self.work.quit()

    def test_upload_images(self):
        self.choose_tool.choose_tool("素材库")
        self.upload.upload_images("C:/Users/CZY/PycharmProjects/Demo/images/起风了.jpg")
        assert self.upload.get_tips() == "OK"