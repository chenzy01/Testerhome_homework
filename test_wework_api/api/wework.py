import requests
import pytest


class WeWork:
    corpid = "wwcd0be06e5dd4dfcb"
    agent = "1"
    contact_secret = "X-2HlpWySBJX2-62G8GQh_i6-c1lom79KySmhglQwxc"
    access_token = None

    @classmethod
    def get_token(cls):
        # get_token 中 access_token 要作为全局变量被调用，get_token 要设置为类级别的方法
        if cls.access_token is None:
            # 获取 token 的url
            url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?"
            r = requests.get(url, params={"corpid": cls.corpid, "corpsecret": cls.contact_secret}).json()
            print("first get token")
            print(r)
            # 把 access_token 设定为类变量，作为全局使用
            cls.access_token = r["access_token"]

        return cls.access_token


