import json

import jsonpath as jsonpath
import requests
from requests import Response


class TestHTTP:
    def test_get(self):
        r = requests.get('https://testerhome.com/hogwarts')
        print(r)

    def test_get_query(self):
        """使用 get() 方法"""
        url = 'http://www.httpbin.org/get'
        payload = {'key1': 'value1', 'key2': 'value2'}
        r = requests.get(url=url, params=payload)
        self.inspect_response(r)

    def test_get_query_headers(self):
        """添加 headers"""
        url = 'http://www.httpbin.org/get'
        payload = {'key1': 'value1', 'key2': 'value2'}
        headers = {'h': '1', "accept": "application/json"}
        r = requests.get(url=url, params=payload, headers=headers)
        self.inspect_response(r)

    def test_post(self):
        """使用 post() 方法"""
        url = 'http://www.httpbin.org/post'
        payload = {'key1': 'value1', 'key2': 'value2'}
        headers = {'h': '1', "accept": "application/json"}
        r = requests.post(url=url, json=payload, headers=headers)
        self.inspect_response(r)

    def test_testerhome(self):
        """测试 testerhome 的帖子"""
        url = "https://testerhome.com/api/v3/topics.json"
        r = requests.get(url=url, params={"limit": "2"})
        # print(r.json())
        # print(r.json()['topics'][0]['id'])
        assert r.json()['topics'][0]['id'] == 22987
        assert r.json()['topics'][1]['user']['login'] == "shixue33"

    def test_test_xuqiu_sogo(self):
        """测试雪球，查找搜狗"""
        url = 'https://xueqiu.com/stock/search.json'
        params = {'code': 'sogo', 'size': 3, 'page': 1}
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
        cookie = 'device_id=24700f9f1986800ab4fcc880530dd0ed; s=dq1jhki0j8; __utma=1.1904762379.1582854658.1582854658.1582854658.1; __utmz=1.1582854658.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); aliyungf_tc=AQAAAHv2xQlJTwMAlO5ocQbYVkKN6ILn; acw_tc=2760823915861005462266183e1ee66aab68b9be2ccaa4a61f06982ae755d5; xq_a_token=2ee68b782d6ac072e2a24d81406dd950aacaebe3; xqat=2ee68b782d6ac072e2a24d81406dd950aacaebe3; xq_r_token=f9a2c4e43ce1340d624c8b28e3634941c48f1052; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTU4NzUyMjY2MSwiY3RtIjoxNTg2MTAwNTMzNjE0LCJjaWQiOiJkOWQwbjRBWnVwIn0.k5nrI7ngqJjI1SIBRcsxJGrO8jKYTNi_4HoCBJ_SmfdGBKIQF2-BuVYOVYR46bmf0quWbhHSWBTePlsAN8Kb5o1l5IApV4e8nONHe3USPl5poxUOaU9w71AmpSQrzl7gGcOyc_j0M2GSgqfvP1yIFxzbEIayt8DwRubI-mQrDhxfZP42NsXR2r8RIHjwHsaesCvtfc1doBnlx1p6KSNIcl-KPcsdETkULKrLPHf9NHcuqStiDFLd3zTBg8xBpVz1-_yGqFuSB9jZ9Xfh1Cx8g8flc9xJnrVDplPFJJrpZZkzKqh1XN8QcXhSYk-Opw_G2f_pLlxegNjePCcGNF0vdg; u=411586100546232; Hm_lvt_1db88642e346389874251b5a1eded6e3=1586100547,1586161425; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1586161749'
        headers = {'User-Agent': user_agent, 'cookie': cookie}
        r = requests.get(url=url, params=params, headers=headers)
        print(r.json())
        assert r.json()['stocks'][0]['name'] == '搜狗'

    def test_get_login_jsonpath(self):
        """使用 jsonpath 断言"""
        url = "https://testerhome.com/api/v3/topics.json"
        data = requests.get(url=url, params={"limit": "2"}).json()
        print(jsonpath.jsonpath(data, "$..user"))

    def inspect_response(self, r: Response):
        print(r.headers)
        print(r.cookies)
        print(r.status_code)
        print(r.encoding)
        print(r.url)
        print(r.content)
        print(r.raw)
        print(r.text)
        print(r.json())



