import base64
import json

import requests


class TestEncode:
    def test_api(self):
        req = ApiRequest()
        req_data = {
            "schema": "http",
            "encoding": "base64",  # 这个字段根据数据格式而定
            "method": "get",
            "url": "http://1.1.1.1/topics.txt",
            "headers": None
        }
        r = req.send(req_data)  # 将数据发送到已封装的函数，返回一个json格式的数据
        assert len(r["topics"]) == 2


class ApiRequest:

    def send(self, data: dict):
        if data["schema"] == "http":
            # 把host修改为IP，并附加到 host header
            # 环境对应关系
            env = {
                "test/dev.com": {
                    "dev": "10.10.10.1",
                    "test": "10.10.10.2",
                },
                "default": "test",
            }
            # 将url中的域名转换为Ip
            data["url"] = str(data["url"]).replace("test/dev.com", env["test/dev.com"][env["default"]])
            data["headers"]["Host"] = "test/dev.com"  # 通过将Host绑上域名，服务器会认为是通过域名进行访问
            res = requests.request(data["method"], data["url"], headers=data["headers"])
            if data["encoding"] == "base64":  # 判断数据的编码格式
                # 使用base64进行解密，将解密后的数据转换成json结构体的数据
                return json.loads(base64.b64decode(res.content))
            else:
                return json.loads(res.content)  # 若数据格式不是base64,将原生内容进行json格式化
        elif data["schema"] == "dubbo":
            pass
        elif data["schema"] == "websocket":
            pass
        else:
            pass
