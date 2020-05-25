
import pytest
import requests
from yaml import load, dump
import test_yaml


def test_yaml():
    env = {
        "test/dev.com": {
            "dev": "10.10.10.1",
            "test": "10.10.10.2",
        },
        "default": "test",
    }
    print(env)
    print(dump(env))  # 将字典结构的数据转换成yaml格式

    yaml_str = """
    default: test
    test/dev.com:
      dev: 10.10.10.1
      test: 10.10.10.2
    """
    print(load(yaml_str))  # load() 将yaml格式的数据转换成字典结构

    f = open("demo.yaml", "rw")  # 可用 with 模式
    print(dump(env, f))


def test_read_yaml_demo():
    with open("demo.yaml", "r") as f:
        print(load(f))


@pytest.mark.parametrize("num", load(open("demo.yaml", "r"))["array"])  # 结合 pytest 参数化方式
def test_yaml_by_pytest(num):
    assert num > 1


class HttpApi:
    def __init__(self, method, url, query):
        self.method = method
        self.url = url
        self.query = query

    def send(self):
        return requests.request(self.method, self.url, params=self.query).json()


def test_get_data():
    # req = HttpApi("get", "https://testerhome.com/api/v3/topics.json", {"limit": 2})

    req: HttpApi = load(open("httpapi.yaml", "r"))
    print(req.send())
    # print(req)
    # print(dump(req))
#    print(req.send())

