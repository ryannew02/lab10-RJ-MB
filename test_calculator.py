#https://github.com/ryannew02/lab10-RJ-MB.git
#Partner 1: Ryan Juergens
#Partner 2: Marcel Bossa

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(3,4), 7)
        self.assertEqual(add(-2,5), 3)
        self.assertEqual(add(0,6),6)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(7,3), 4)
        self.assertEqual(subtract(3,5), -2)
        self.assertEqual(subtract(5, 8), -3)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        #testing general Multiplication
        self.assertEqual(mul(5, 3), 15)
        #testing Identity property
        self.assertEqual(mul(1,12), 12)
        #testing zero property
        self.assertEqual(mul(0, 12), 0)
    def test_divide(self): # 3 assertions
        #testing regular division
        self.assertAlmostEqual(div(2,9), 4.5)
        #testing division by 1
        self.assertEqual(div(1,10), 10)
        #testing division by larger dividend
        self.assertAlmostEqual(div(10, 2), .2)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0,5)
        # call division function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     div(0, 5)
        #fill in code

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(10,1), 0)
        self.assertAlmostEqual(logarithm(2, 3), 1.585, places=3)
        self.assertAlmostEqual(logarithm(7,6), 0.9208, places=4 )

        #fill in code

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0,6)
        # use same technique from test_divide_by_zero
        #fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        #test simple hypotenuse
        self.assertEqual(hypotenuse(3,4), 5)
        #test complex hypotenuse
        self.assertAlmostEqual(hypotenuse(4,4), 5.6568542, places=7)
        #test 0 case
        self.assertEqual(hypotenuse(0,4), 4)
    def test_sqrt(self): # 3 assertions
        #test for complex square root
        self.assertAlmostEqual(square_root(24), 4.89897948, places=7)
        #test for simple square root
        self.assertEqual(square_root(9), 3)
        #test for invalid argument
        with self.assertRaises(ValueError):
           square_root(-16)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()