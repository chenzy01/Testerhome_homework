import pytest

from test_wework_api.api.wework import WeWork


class TestWeWork:
    def test_get_token(self):
        wework = WeWork()
        token = wework.get_token()
        assert token is not None
