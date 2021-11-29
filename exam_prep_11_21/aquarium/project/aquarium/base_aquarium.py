from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        result = 0
        for decoration in self.decorations:
            result += decoration.comfort
        return result

    def add_fish(self, fish):
        if len(self.fish) >= self.capacity:
            return "Not enough capacity."
        fish_type = fish.__class__.__name__
        aquarium_type = self.__class__.__name__
        if fish_type[:9] == aquarium_type[:9]:
            self.fish.append(fish)
            return f"Successfully added {fish_type} to {self.name}."
        return "Water not suitable."

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        result = f"{self.name}:\n"
        if self.fish:
            result += f"Fish: {' '.join([fish.name for fish in self.fish])}\n"
        else:
            result += "Fish: none\n"
        result += f"Decorations: {len(self.decorations)}\nComfort: {self.calculate_comfort()}"
        return result

