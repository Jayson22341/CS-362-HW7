import unittest
import FizzBuzz

class FizzBuzzTest(unittest.TestCase):
    def test_base(self):
        result = FizzBuzz.FizzBuzz(1)
        self.assertEqual(result, 1)
    def test_three(self):
        result = FizzBuzz.FizzBuzz(3)
        self.assertEqual(result,"Fizz")
    def test_five(self):
        result = FizzBuzz.FizzBuzz(5)
        self.assertEqual(result,"Buzz")
    def test_three_and_five(self):
        result = FizzBuzz.FizzBuzz(15)
        self.assertEqual(result,"FizzBuzz")

if __name__ == "__main__":
    unittest.main()
