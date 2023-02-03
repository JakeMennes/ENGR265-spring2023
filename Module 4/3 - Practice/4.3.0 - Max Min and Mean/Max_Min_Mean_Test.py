import unittest
import Max_Min_Mean as pp


class TestIfAssignment(unittest.TestCase):

    def test_max(self):
        self.assertNotEqual(pp.list_max, -1, "Did you change your answer?")
        self.assertEquals(pp.list_max, 112)

    def test_min(self):
        self.assertNotEqual(pp.list_min, -1, "Did you change your answer?")
        self.assertEquals(pp.list_min, 2)

    def test_average(self):
        self.assertNotEqual(pp.list_average, -1, "Did you change your answer?")
        self.assertAlmostEqual(pp.list_average, 49.86)


if __name__ == '__main__':
    unittest.main()
