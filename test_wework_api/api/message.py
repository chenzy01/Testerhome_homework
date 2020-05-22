import requests

from test_wework_api.api.BaseApi import BaseApi
from test_wework_api.api.wework import WeWork


class Message(BaseApi):
    # 发送消息接口地址
    _send_url = "https://qyapi.weixin.qq.com/cgi-bin/message/send"

    # 发送文本消息
    def send_text(self, msg=None, users=[], parties=[], tags=[], ):
        self.json_data = requests.post(self._send_url, params={"access_token": WeWork.get_token()}, json={
           "touser": "|".join(users),
           "toparty": "|".join(parties),
           "totag": "|".join(tags),
           "msgtype": "text",
           "agentid": 1,
           "text": {
               "content": msg
           },
           "safe": 0,
           "enable_id_trans": 0,
           "enable_duplicate_check": 0,
           "duplicate_check_interval": 1800
        }).json()
        self.verbose(self.json_data)  # 这里的verbose 函数是类函数，传递的参数是一个类变量

    def send_voice(self):
        pass

    def send_video(self):
        pass