from test_wework_api.api.message import Message


class TestMessage:
    msg = Message()
    content = "你的快递已到，请携带工卡前往邮件中心领取。\n出发前可查看<a href=\"http://work.weixin.qq.com\">邮件中心视频实况</a>，聪明避开排队。"

    def test_send_text(self):
        # 测试发送消息文本,注意接收人要在应用的可见范围内，通过应用管理>点击相关应用>可见范围
        # 若是接收人的账号非真实微信或虚拟创建的，则可能返回：invaliduser
        self.msg.send_text(msg=self.content,
                           users=["ChenZhenYang", "002"])
        assert self.msg.json_path("$.errcode") == 0
