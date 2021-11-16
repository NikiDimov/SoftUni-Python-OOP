class Animal:
    _sound = None
    _species = None

    def get_species(self):
        return self._species

    def get_sound(self):
        return self._sound


class Dog(Animal):
    _sound = 'woof-woof'
    _species = 'dog'


class Cat(Animal):
    _sound = 'meow'
    _species = 'cat'


def animal_sound(animals: list):
    for animal in animals:
        print(animal.get_sound())


animals = [Cat(), Dog()]
animal_sound(animals)
