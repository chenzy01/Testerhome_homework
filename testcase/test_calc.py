import unittest
from src.calc import Calc
from ddt import ddt, data, unpack, file_data
import yaml


@ddt
class TestCalc(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = Calc()

    @data((1, 1, 2),
          (1, 0, 1),
          (0.4, 1, 1.4),
          (1000, 1, 1001),
          (-1, 1, 0))
    @unpack
    def test_add(self, a, b, c):
        self.assertEqual(self.calc.add(a, b), c)

    @file_data('calc.yaml')
    def test_div(self, a, b, c):
        result = self.calc.div(a, b)
        self.assertEqual(result, c)

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









