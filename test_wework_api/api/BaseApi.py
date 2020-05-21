from test_wework_api.utils.Utils import Utils
import pprint


class BaseApi:
    json_data = None

    @classmethod
    def verbose(cls, json_object=json_data):
        print(Utils.json_format(json_object))

    @classmethod
    def json_path(cls, expr):
        return Utils.json_path(cls.json_data, expr)

