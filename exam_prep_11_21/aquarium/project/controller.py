from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type, aquarium_name):
        valid_aquariums = ["FreshwaterAquarium", "SaltwaterAquarium"]
        if aquarium_type not in valid_aquariums:
            return "Invalid aquarium type."
        new_aquarium = None
        if aquarium_type == "FreshwaterAquarium":
            new_aquarium = FreshwaterAquarium(aquarium_name)
        elif aquarium_type == "SaltwaterAquarium":
            new_aquarium = SaltwaterAquarium(aquarium_name)
        self.aquariums.append(new_aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type):
        valid_decorations = ["Ornament", "Plant"]
        if decoration_type not in valid_decorations:
            return "Invalid decoration type."
        if decoration_type == "Ornament":
            self.decorations_repository.add(Ornament())
        elif decoration_type == "Plant":
            self.decorations_repository.add(Plant())
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name, decoration_type):
        decoration = self.decorations_repository.find_by_type(decoration_type)
        if decoration == "None":
            return f"There isn't a decoration of type {decoration_type}."
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                aquarium.decorations.append(decoration)
                self.decorations_repository.remove(decoration)
                return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name, fish_type, fish_name, fish_species, price):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                if fish_type == "FreshwaterFish":
                    return aquarium.add_fish(FreshwaterFish(fish_name, fish_species, price))
                elif fish_type == "SaltwaterFish":
                    return aquarium.add_fish(SaltwaterFish(fish_name, fish_species, price))
                return f"There isn't a fish of type {fish_type}."

    def feed_fish(self, aquarium_name):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                aquarium.feed()
                return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                value = 0
                for decoration in aquarium.decorations:
                    value += decoration.price
                for fish in aquarium.fish:
                    value += fish.price
                return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        result = ''
        for aquarium in self.aquariums:
            result += f"{aquarium}\n"
        return result






# c = Controller()
# c.add_aquarium("FreshwaterAquarium", "The Fish")
# c.add_decoration("Ornament")
# c.add_decoration("Plant")
# print(c.decorations_repository.decorations)
# print(c.insert_decoration("The Fish", "Ornament"))
# print(c.insert_decoration("The Fish", "Plant"))
# print(c.decorations_repository.decorations)
# print(c.add_fish("The Fish", "FreshwaterFish", "Niki", "Shark", 10))
# print(c.add_fish("The Fish", "FreshwaterFish", "Pesho", "Shark", 20))
# print(c.feed_fish("The Fish"))
# c.add_aquarium("FreshwaterAquarium", "Johny")
# print(c.report())


