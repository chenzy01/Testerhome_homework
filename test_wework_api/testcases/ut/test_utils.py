import pytest
import requests

from test_wework_api.utils.Utils import Utils


class TestUtils:
    def test_json_format(self):
        print(Utils.json_format({"a": "1", "b": {"c": "111"}}))

    def test_jsonpath(self):
        r = requests.get("https://testerhome.com/api/v3/topics.json?limit=2").json()
        assert Utils.json_path(r, "$.topics[?(@.excellent == 0)]")[0]["id"] > 20000
