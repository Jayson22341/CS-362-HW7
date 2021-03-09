import unittest
import LeapYear

class LeapYearTest(unittest.TestCase):
    def test_base(self):
        result = LeapYear.YearCheck(1)
        self.assertEqual(result, False)

if __name__ == "__main__":
    unittest.main()
