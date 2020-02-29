import pytest
import requests
import logging

logging.basicConfig(level=logging.DEBUG)


@pytest.fixture()
def topics():
    url = "http://127.0.0.1:8000/topics.json"
    logging.info(url)
    # URL = "https://testerhome.com/api/v3/topics.json?limit=2"
    yield requests.get(url).json()
    logging.info("after yield")


@pytest.fixture(params=["http://127.0.0.1:8000/topics.json",
                        "https://testerhome.com/api/v3/topics.json?limit=2"])
def topics2(request):
    url = request.param
    # url = "http://127.0.0.1:8000/topics.json"
    logging.info(url)

    # URL = "https://testerhome.com/api/v3/topics.json?limit=2"

    def fin():  # 这一部分模拟teardown
        logging.info("after yield teardown")

    request.addfinalizer(fin)
    return requests.get(url).json()


@pytest.fixture(scope="module")
def fixture_module_setup_classA():
    logging.info("module setup")
    yield
    logging.info("module teardown")


@pytest.fixture(scope="class")
def fixture_class_teardown_classA():
    logging.info("classA setup")
    yield
    logging.info("classA teardown")


@pytest.fixture(scope="function")
def fixture_method_test4():
    logging.info("test4 setup")


@pytest.fixture(scope="function", params=[
    (3, 4, 12),
    (2.5, 3, 7.5),
    (2, -1, -2)
])
def fixture_method_test5(request):
    logging.info("test5 数据参数化")
    yield request.param
