import unittest
from fizzbuzz import *

class TestFizzBuzz(unittest.TestCase):

    def test_returns_fizz_with_num_divisibl3_by_3(self):
        self.assertEqual(fizzbuzz.says(3), 'Fizz')

if __name__ == '__main__':
    unittest.main()
