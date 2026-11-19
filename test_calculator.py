# https://github.com/Ebird1912/lab11-ES (completed individually, I had an issue with my origonal partner and didnt have time to find a new one)
# Partner 1: Ethan Simon

import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-4, 1), -3)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(9, 4), 5)
        self.assertEqual(subtract(3, 7), -4)
        self.assertEqual(subtract(-2, -5), 3)

    def test_multiply(self): 
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(10, 0), 0)

    def test_divide(self): 
        self.assertEqual(div(12, 3), 4)
        self.assertEqual(div(-15, 5), -3)
        self.assertEqual(div(5, 2), 2.5)

    def test_divide_by_zero(self): 
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self): 
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(3, 27), 3)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(0, 5)


    def test_log_invalid_argument(self): 
        with self.assertRaises(ValueError):
            logarithm(2, 0)

    def test_hypotenuse(self): 
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertEqual(hypotenuse(0, 7), 7)

    def test_sqrt(self):
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(0), 0)
        with self.assertRaises(ValueError):
            square_root(-4)


if __name__ == "__main__":
    unittest.main()
