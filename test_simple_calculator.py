import unittest

from simple_calculator import calculate


class TestSimpleCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculate(1, "+", 2), 3.0)

    def test_subtract(self):
        self.assertEqual(calculate(5, "-", 3), 2.0)

    def test_multiply_star(self):
        self.assertEqual(calculate(4, "*", 2), 8.0)

    def test_multiply_x(self):
        self.assertEqual(calculate(4, "x", 2), 8.0)

    def test_divide(self):
        self.assertEqual(calculate(8, "/", 4), 2.0)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ZeroDivisionError):
            calculate(5, "/", 0)

    def test_integer_floor_div(self):
        self.assertEqual(calculate(7, "//", 3), 2.0)

    def test_modulo(self):
        self.assertEqual(calculate(7, "%", 3), 1.0)

    def test_power(self):
        self.assertEqual(calculate(2, "**", 3), 8.0)

    def test_invalid_operator_raises(self):
        with self.assertRaises(ValueError):
            calculate(1, "?", 2)


if __name__ == "__main__":
    unittest.main()
