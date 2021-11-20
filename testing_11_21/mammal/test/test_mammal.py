from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.animal = Mammal('Tom', 'cat', 'meow')

    def test_initialization(self):
        self.assertEqual('Tom', self.animal.name)
        self.assertEqual('cat', self.animal.type)
        self.assertEqual('meow', self.animal.sound)
        self.assertEqual('animals', self.animal._Mammal__kingdom)

    def test_making_sound(self):
        self.assertEqual("Tom makes meow", self.animal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual('animals', self.animal.get_kingdom())

    def test_get_info(self):
        self.assertEqual('Tom is of type cat', self.animal.info())


if __name__ == '__main__':
    main()
