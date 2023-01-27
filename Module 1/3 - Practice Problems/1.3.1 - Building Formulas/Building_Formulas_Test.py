# tests the final balance of the account after interest
# this unittest would be identical to the one used by math package
import unittest
import Building_Formulas as bf


class TestFormulas(unittest.TestCase):
    def testone_num(self):
        self.assertIsNotNone(bf.step_one, msg="Did you change step_one's value?")
        self.assertAlmostEqual(bf.step_one, 0.01)

    def test_two_num(self):
        self.assertIsNotNone(bf.step_two, msg="Did you change step_two's value?")
        self.assertAlmostEqual(bf.step_two, 1.1046221254112045)

    def test_three_num(self):
        self.assertIsNotNone(bf.step_three, msg="Did you change step_three's value?")
        self.assertAlmostEqual(bf.step_three, 1104.6221254112045)

    def test_growth(self):
        self.assertIsNotNone(bf.growth, msg="Did you change growth's value?")
        self.assertAlmostEqual(bf.growth, 60343.922499999986)


if __name__ == '__main__':
    unittest.main()
