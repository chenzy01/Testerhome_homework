import pytest
import logging


logging.basicConfig(level=logging.DEBUG)


@pytest.mark.usefixtures("fixture_module_setup_classA")
@pytest.mark.usefixtures("fixture_class_teardown_classA")
@pytest.mark.run(order=1)
class TestA:

    def test_1(self):
        print("This is test1")

    def test_2(self):
        print("This is test2")

    def test_3(self):
        print("This is test3")


@pytest.mark.run(order=2)
class TestB:

    def test_4(self, fixture_method_test4):
        print("This is test4")

    def test_5(self, fixture_method_test5):
        # print (fixture_method_test5)
        a, b, c = fixture_method_test5
        assert a * b == c
