import unittest
import LeapYear

class LeapYearTest(unittest.TestCase):
    def test_base(self):
        result = LeapYear.YearCheck(1)
        self.assertEqual(result, False)
    def test_four(self):
        result = LeapYear.YearCheck(4)
        self.assertEqual(result, True)

if __name__ == "__main__":
    unittest.main()
