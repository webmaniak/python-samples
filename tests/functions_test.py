import unittest
from .context import functions as f

class FunctionTestCase(unittest.TestCase):
    """A bunch of tests meant to check functions.py's behavior."""

    def setUp(self):
        pass

    def test_uppercase_first_letter(self):
        test_input = 'hello'
        result = f.uppercase_first_letter(test_input)
        self.assertEqual('Hello', result)

    def test_concat_strings(self):
        first_string = 'hello'
        second_string = 'world'
        result = f.concat_strings(first_string, second_string)
        self.assertEqual('helloworld', result)

    def test_make_list(self):
        reference_list = ['a','b','c']
        result = f.make_list('a', 'b', 'c')
        self.assertCountEqual(result, reference_list)
        self.assertListEqual(reference_list, result)

if __name__ == '__main__':
    unittest.main()