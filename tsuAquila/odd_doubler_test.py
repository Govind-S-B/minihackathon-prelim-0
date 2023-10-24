# odd_doubler_test.py
import unittest
from odd_doubler import odd_doubler

class TestOddDoublerFunction(unittest.TestCase):

    def test_1_integers(self):
        input_list = [1, 2, 3, 4, 5]
        expected_output = [2, 2, 6, 4, 10]
        self.assertEqual(odd_doubler(input_list), expected_output)

    def test_2_integers(self):
        input_list = [1,5,2,6,7]
        expected_output = [2, 10, 2, 6, 14]
        self.assertEqual(odd_doubler(input_list), expected_output)

    def test_3_integers(self):
        input_list = [1,2,4,6]
        expected_output =[2, 2, 4, 6]
        self.assertEqual(odd_doubler(input_list), expected_output)

    def test_empty_list(self):
        input_list = []
        expected_output = []
        self.assertEqual(odd_doubler(input_list), expected_output)



if __name__ == '__main__':
    unittest.main()
