from unittest import TestCase, main

# from OOP.testing.mammal.project.mammal import Mammal


from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal_1 = Mammal("George", "dog", "woof")

    def test_attr_are_set(self):
        self.assertEqual("George", self.mammal_1.name)
        self.assertEqual("dog", self.mammal_1.type)
        self.assertEqual("woof", self.mammal_1.sound)
        self.assertEqual("animals", self.mammal_1._Mammal__kingdom)

    def test_sound(self):
        self.assertEqual("George makes woof", self.mammal_1.make_sound())

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal_1.get_kingdom())

    def test_get_animal_info(self):
        self.assertEqual("George is of type dog", self.mammal_1.info())


if __name__ == "__main__":
    main()
