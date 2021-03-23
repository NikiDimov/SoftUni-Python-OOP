from OOP.inheritance.hierarchical_inheritance.animal import Animal


class Cat(Animal):
    def meow(self):
        return "meowing..."


cat = Cat()
print(cat.eat())
