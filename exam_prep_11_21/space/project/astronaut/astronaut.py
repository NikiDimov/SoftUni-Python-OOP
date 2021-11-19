from abc import ABC, abstractmethod


class Astronaut(ABC):
    oxygen_units = 10

    @abstractmethod
    def __init__(self, name, oxygen):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '' or value == ' ':
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    def back_pack(self):
        if self.backpack:
            return ', '.join(self.backpack)
        return 'none'

    def breathe(self):
        self.oxygen -= self.oxygen_units

    def increase_oxygen(self, amount):
        self.oxygen += amount

    def __repr__(self):
        result = f"Name: {self.name}\nOxygen: {self.oxygen}\nBackpack items: {self.back_pack()}"
        return result
