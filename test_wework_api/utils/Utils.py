import json

from jsonpath import jsonpath


class Utils:
    """对数据格式通用处理"""

    @classmethod
    def json_format(cls, json_object):
        # 将数据转换为 json 格式
        return json.dumps(json_object, indent=2)

    @classmethod
    def json_path(cls, json_object, expr):
        # 使用 jsonpath 来解析内容
        return jsonpath(json_object, expr)
