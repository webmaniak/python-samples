import unittest
from animals import Dog

class DogTestClass(unittest.TestCase):
    """Tests for animals.py"""

    def setUp(self):
        self.dog = Dog("Barry", 5)

    def test_dog_name(self):
        self.assertEqual(self.dog.name, "Barry")

    def test_dog_age(self):
        self.assertEqual(self.dog.age, 5)

#unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(DogTestClass)
unittest.TextTestRunner(verbosity=2).run(suite)