import unittest
import main


class Testmain(unittest.TestCase):
    def setUp(self):
        print('About to test')

    def test_case_1(self):
        test_param = 5
        result = main.do_stuff(test_param)
        self.assertEqual(result, 10)

    def test_case_2(self):
        test_param = 'ovoisdnvonvo'
        result = main.do_stuff(test_param)
        self.assertTrue(isinstance(result, ValueError))

    def test_case_3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please enter a number')

    def test_case_4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please enter a number')

    def tearDown(self):
        print('Tearding down the test case')

# If we provide unittest.main() it will run the whole file as it is a test file.


if(__name__ == '__main__'):
    unittest.main()
