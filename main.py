import unittest
from SimpleCalculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.simple_calculator = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.simple_calculator.add(8, 9), 17)

    def test_multiply(self):
        self.assertEqual(self.simple_calculator.multiply(4, 7), 28)

    def test_subtract(self):
        self.assertEqual(self.simple_calculator.subtract(39, 8), 31)

    def test_devide(self):
        self.assertEqual(self.simple_calculator.divide(90, 10), 9)

if __name__ == "__main__":
    unittest.main()



