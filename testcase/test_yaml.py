import yaml
import json


def test_json():
    print(json.load(open("calc.json")))


def test_yaml():
    print(yaml.load(open("calc2.yaml")))
