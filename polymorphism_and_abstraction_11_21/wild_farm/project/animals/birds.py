from project.animals.animal import Bird


class Owl(Bird):
    foods = ["Meat"]
    weight_constant = 0.25

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    foods = ["Meat", "Vegetable", "Fruit", "Seed"]
    weight_constant = 0.35

    def make_sound(self):
        return "Cluck"
