import unittest
import List_Assignment as pp


class TestListSlicing(unittest.TestCase):

    def test_fives_list(self):
        self.assertIsNotNone(pp.fives_list, "Did you change fives_list?")
        self.assertEqual(pp.fives_list, [5, 10, 15, 20])

    def test_tail(self):
        self.assertIsNotNone(pp.tail, "Did you change tail?")
        self.assertEqual(pp.tail, 20)

    def test_new_list(self):
        self.assertNotEqual(pp.new_list, [1, 2, 3, 4, 5], "Did you add values to new_list?")
        self.assertEqual(pp.new_list, [0, 1, 2, 3, 4, 5, 6])

    def test_first_two(self):
        self.assertIsNotNone(pp.first_two, "Did you change first_two?")
        self.assertEqual(pp.first_two, ["Luke", "Leia"])

    def test_last_three(self):
        self.assertIsNotNone(pp.last_three, "Did you change last_three?")
        self.assertEqual(pp.last_three, ["Han", "Vader", "R2D2"])

    def test_slicing_copy(self):
        self.assertIsNotNone(pp.slicing_copy, "Did you change slicing_copy?")
        self.assertEqual(pp.slicing_copy, ["Luke", "Leia", "Han", "Vader", "R2D2"])


if __name__ == '__main__':
    unittest.main()
