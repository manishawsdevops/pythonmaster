import unittest
import randomgame


class TestGame(unittest.TestCase):
    def setUp(self):
        print('Testing Random Game')

    def test_case_1(self):
        guess = 5
        answer = 5
        result = randomgame.run_guess(guess, answer)
        self.assertTrue(result)


# If we provide unittest.main() it will run the whole file as it is a test file.


if(__name__ == '__main__'):
    unittest.main()
