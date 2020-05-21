from test_wework_api.api.message import Message


class TestMessage:
    msg = Message()
    content = "你的快递已到，请携带工卡前往邮件中心领取。\n出发前可查看<a href=\"http://work.weixin.qq.com\">邮件中心视频实况</a>，聪明避开排队。"

    def test_send_text(self, content=None):
        # 测试发送消息文本
        self.msg.send_text(content,
                           users=["ChenZhenYang"])
        assert self.msg.json_path("$.errcode") == 0
