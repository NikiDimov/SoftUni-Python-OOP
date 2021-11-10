from project.animals.animal import Mammal


class Mouse(Mammal):
    foods = ["Vegetable", "Fruit"]
    weight_constant = 0.10

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    foods = ["Meat"]
    weight_constant = 0.40

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    foods = ["Meat", "Vegetable"]
    weight_constant = 0.30

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    foods = ["Meat"]
    weight_constant = 1

    def make_sound(self):
        return "ROAR!!!"
