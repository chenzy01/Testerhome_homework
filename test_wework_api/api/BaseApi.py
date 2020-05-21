from test_wework_api.utils.Utils import Utils
import pprint


class BaseApi:
    def verbose(self, json_object):
        print(Utils.json_format(json_object))
