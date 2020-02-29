import unittest
from src.calc import Calc
from ddt import ddt, data, unpack, file_data
import yaml
import pytest
import json
import yaml


class TestCalc():

    def setup(self) -> None:
        self.calc = Calc()

    @pytest.mark.parametrize("a, b, c", [
        (1, 1, 2),
        (1, 0, 1),
        (0.4, 1, 1.4),
        (1000, 1, 1001),
        (-1, 1, 0)
    ])
    def test_add(self, a, b, c):
        assert self.calc.add(a, b) == c

    # @file_data('calc.yaml')
    @pytest.mark.parametrize("a, b, c", yaml.load(open("calc2.yaml")))
    def test_div(self, a, b, c):
        assert self.calc.div(a, b) == c

    def test_above(self):
        result = self.calc.above(100, 1)
        self.assertEqual(result, True)

        result = self.calc.above(1, 3)
        self.assertEqual(result, False)

        result = self.calc.above(3.3, 3)
        self.assertEqual(result, True)

        result = self.calc.above(0, -3)
        self.assertEqual(result, True)

        result = self.calc.above(-2, -3)
        self.assertEqual(result, True)

        result = self.calc.above(-5, -3)
        self.assertEqual(result, False)









