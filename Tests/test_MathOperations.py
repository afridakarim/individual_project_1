import unittest

from MathOperations.addition import Addition
from MathOperations.subtraction import Subtraction
from MathOperations.multiplication import Multiplication


class MyTestCase(unittest.TestCase):

    def test_MathOperations_addition(self):
        self.assertEqual(3, Addition.sum(1, 2))

    def test_MathOperations_subtraction(self):
        self.assertEqual(-1, Subtraction.difference(1, 2))

    def test_MathOperations_multiplication(self):
        self.assertEqual(4,Multiplication.product(2,2))

    def test_MathOperations_sum_list(self):
        valuelist = [1, 2, 3]
        self.assertEqual(6, Addition.sum(valuelist))

    def test_MathOperations_difference_list(self):
        differenceValueList = [3,2,1]
        self.assertEqual(-6,Subtraction.difference(differenceValueList))

    def test_MathOperations_product_list(self):
        multiplicationValueList = [0,0,0]
        self.assertEqual(0,Multiplication.product(multiplicationValueList))


if __name__ == '__main__':
    unittest.main()