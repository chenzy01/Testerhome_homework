import pytest
import logging

# import allure

logging.basicConfig(level=logging.DEBUG)


def setup_module():
    logging.info("模块初始化")


def teardown_module():
    logging.info("模块结束清理")


@pytest.mark.run(order=1)
class TestA:

    @classmethod
    def setup_class(cls):
        logging.info("TestA 初始化")

    def test_1(self):
        pass

    def test_2(self):
        pass

    def test_3(self):
        pass

    @classmethod
    def teardown_class(cls):
        logging.info("TestA 测试结束，环境清理")


@pytest.mark.run(order=2)
class TestB:

    def setup_method(self):
        logging.info("TestB 用例初始化")

    def test_4(self):
        pass

    @pytest.mark.parametrize('a, b, c', [
        (3, 4, 12),
        (2.5, 3, 7.5),
        (2, -1, -2)
    ])
    def test_5(self, a, b, c):
        assert a * b == c

    @pytest.mark.parametrize("a, b, c", [
        (1, 1, 2),
        (1, 0, 1),
        (0.4, 1, 1.4),
    ])
    def test_6(self, a, b, c):
        assert a + b == c


@pytest.mark.run(order=3)
class TestC:

    @pytest.mark.run(order=3)
    def test_7(self):
        pass

    @pytest.mark.run(order=1)
    def test_8(self):
        pass

    @pytest.mark.run(order=2)
    def test_9(self):
        pass


if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', 'C:/Users/CZY/PycharmProjects/Demo/report'])
