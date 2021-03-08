import unittest
import FizzBuzz

class FizzBuzzTest(unittest.TestCase):
    def test_base(self):
        result = FizzBuzz.FizzBuzz(1)
        self.assertEqual(result, 1)

if __name__ == "__main__":
    unittest.main()
