import requests


from test_wework_api.utils.Utils import Utils
import pprint


class BaseApi:
    json_data = None
    proxies = {"http": "http://127.0.0.1:8888", "https": "http://127.0.0.1:8888"}

    @classmethod
    def verbose(cls, json_object=json_data):
        # 将数据转换为 json 格式
        print(Utils.json_format(json_object))

    @classmethod
    def json_path(cls, expr):
        # 使用 jsonpath 对内容进行定位，expr 是要定位的内容
        return Utils.json_path(cls.json_data, expr)

    def request(self, method, url, params: dict, json, data):
        from test_wework_api.api.wework import WeWork
        self.json_data = requests.request(method, url=url,
                                          params=params.update({"access_token": WeWork.get_app_token()}))
        self.verbose(self.json_data)
        return self.json_data



