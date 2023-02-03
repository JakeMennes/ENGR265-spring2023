import unittest
import If_Assignment as pp


class TestIfAssignment(unittest.TestCase):

    def test_case_one(self):
        answer = "Option Three"
        self.assertNotEqual(pp.case_one_answer, "Your Answer Here", "Did you input your answer?")
        self.assertEqual(pp.case_one_answer, answer)

    def test_case_two(self):
        answer = "It's nice out"
        self.assertNotEqual(pp.case_two_answer, "Your Answer Here", "Did you input your answer?")
        self.assertEquals(pp.case_two_answer, answer)


if __name__ == '__main__':
    unittest.main()
