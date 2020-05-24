import requests
import pytest
from test_wework_api.api.base_api import BaseApi


class WeWork(BaseApi):
    corpid = "wwcd0be06e5dd4dfcb"
    agent_id = "1000002"
    agent_secret = "CGdpcf0_Y2bLpc4vT2_YqZoQUaG25u4K42caEBnmEmc"
    contact_secret = "X-2HlpWySBJX2-62G8GQh_i6-c1lom79KySmhglQwxc"
    access_token_contact = None
    access_token_app = None

    @classmethod
    def get_token(cls):
        # get_token 中 access_token 要作为全局变量被调用，get_token 要设置为类级别的方法
        if cls.access_token_contact is None:
            # 获取 token 的url
            url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?"
            r = requests.get(url, params={"corpid": cls.corpid, "corpsecret": cls.contact_secret}).json()
            print("first get token")
            cls.verbose(r)
            # 把 access_token 设定为类变量，作为全局使用
            cls.access_token_contact = r["access_token"]

        return cls.access_token_contact

    @classmethod
    def get_app_token(cls):
        # get_token 中 access_token 要作为全局变量被调用，get_token 要设置为类级别的方法
        if cls.access_token_app is None:
            # 获取 token 的url
            url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?"
            r = requests.get(url, params={"corpid": cls.corpid, "corpsecret": cls.agent_secret}).json()
            print("first get token")
            cls.verbose(r)
            # 把 access_token 设定为类变量，作为全局使用
            cls.access_token_app = r["access_token"]

        return cls.access_token_app


