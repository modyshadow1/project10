import unittest

from calculator import calculate


class TestCalculator(unittest.TestCase):

    # Addition tests
    def test_addition_positive_numbers(self):
        self.assertEqual(calculate(5, 3, "+"), 8)

    def test_addition_negative_numbers(self):
        self.assertEqual(calculate(-5, -3, "+"), -8)

        def test_unsupported_operation_raises_error(self):
        with self.assertRaises(ValueError):
            calculate(5, 2, "//")

    def test_empty_operation_raises_error(self):
        with self.assertRaises(ValueError):
            calculate(5, 2, "")

    def test_string_operand_raises_error(self):
        with self.assertRaises(TypeError):
            calculate("5", 2, "+")

    def test_none_operand_raises_error(self):
        with self.assertRaises(TypeError):
            calculate(None, 2, "+")

    def test_boolean_operand_raises_error(self):
        with self.assertRaises(TypeError):
            calculate(True, 2, "+")


if __name__ == "__main__":
    unittest.main()
