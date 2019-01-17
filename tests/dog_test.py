import unittest
from classes.animals import Dog

class DogTestClass(unittest.TestCase):
    """Tests for animals.py"""

    def setUp(self):
        self.dog = Dog("Barry", 5, 'Golden Retriever')

    def test_dog_name(self):
        self.assertEqual(self.dog.name, "Barry")

    def test_dog_age(self):
        self.assertEqual(self.dog.age, 5)

    def test_dog_breed(self):
        self.assertEqual(self.dog.breed, 'Golden Retriever')

    def test_dog_str(self):
        expected_result = f'This is an animal called {self.dog.name}' \
                f' aged of {str(self.dog.age)} years.'
        self.assertEqual(str(self.dog), expected_result)

    def test_dog_repr(self):
        expected_result = f'Dog({self.dog.name!r}, {self.dog.age!r}, ' \
                            f'{self.dog.breed!r})'
        self.assertEqual(repr(self.dog), expected_result)

if __name__ == '__main__':
    unittest.main()

#suite = unittest.TestLoader().loadTestsFromTestCase(DogTestClass)
#unittest.TextTestRunner(verbosity=2).run(suite)