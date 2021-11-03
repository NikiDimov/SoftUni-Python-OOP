class Animal:
    money_for_care = None

    def __init__(self, name, gender, age):
        self.age = age
        self.gender = gender
        self.name = name

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"



