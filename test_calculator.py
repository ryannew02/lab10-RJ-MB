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
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
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
        self.assertEqual(logrithm(10,1), 0)
        self.assertAlmostEqual(logrithm(2, 3), 1.585, places=3)
        self.assertAlmostEqual(logrithm(7,6), 0.9208, places=4 )

        #fill in code

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0,6)
        # use same technique from test_divide_by_zero
        #fill in code
    # ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()