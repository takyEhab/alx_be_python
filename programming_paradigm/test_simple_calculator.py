import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -2), -3)
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(7, 2), 5)
        self.assertEqual(self.calc.subtract(3, 3), 0)
        self.assertEqual(self.calc.subtract(3, -3), 6)
        self.assertEqual(self.calc.subtract(2, 7), -5)
    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-1, -2), 2)
        self.assertEqual(self.calc.multiply(0, 10), 0)
        self.assertEqual(self.calc.multiply(10, 0), 0)
    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(3, 3), 1)
        self.assertEqual(self.calc.divide(3, -3), -1)
        self.assertEqual(self.calc.divide(2, 7), 2/7)
        self.assertEqual(self.calc.divide(0, 10), 0)
        self.assertEqual(self.calc.divide(10, 0), None)
