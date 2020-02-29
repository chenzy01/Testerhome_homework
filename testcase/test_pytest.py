import logging

import pytest

logging.basicConfig(level=logging.DEBUG)


def setup_module():
    logging.info("setup module")


def teardown_module():
    logging.info("teardown module")


class TestPytestObject2:
    def test_three(self):
        assert [1, 2] == [1, 3]

    def test_foure(self):
        assert {"a": 1, "b": "ssss"} == {"a": 2, "b": "ss"}


class TestPytestObject:

    @classmethod
    def setup_class(cls):
        logging.info("setup class")

    def setup_method(self):
        logging.info("setup method")

    @pytest.mark.run(order=2)
    def test_two(self):
        assert 1 == 2

    @pytest.mark.run(order=1)
    def test_one(self):
        assert True == False

    def teardown_method(self):
        logging.info("teardown method")

    @classmethod
    def teardown_class(cls):
        logging.info("teardown class")
