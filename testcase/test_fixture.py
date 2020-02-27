import pytest
import requests
import logging

# @pytest.fixture(scope="session")
# def topics():
#     url = "http://127.0.0.1:8080/topics.json"
#     # URL = "https://testerhome.com/api/v3/topics.json?limit=2"
#     return requests.get(url).json()


def test_1(topics):
    logging.info("start")
    assert len(topics["topics"]) == 2
    logging.info("end")


def test_2(topics):
    assert topics["topics"][0]["deleted"] == False
