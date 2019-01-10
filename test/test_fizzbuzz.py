import unittest
from lib.fizzbuzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):

    def test_returns_fizz_with_num_divisible_by_3(self):
        fizzbuzz = FizzBuzz()
        self.assertEqual(fizzbuzz.says(3), 'Fizz')

    def test_returns_buzz_with_num_divisible_by_5(self):
        fizzbuzz = FizzBuzz()
        self.assertEqual(fizzbuzz.says(5), 'Buzz')

    def test_returns_fizzbuzz_with_num_divisible_by_15(self):
        fizzbuzz = FizzBuzz()
        self.assertEqual(fizzbuzz.says(15), 'FizzBuzz')

if __name__ == '__main__':
    unittest.main()
