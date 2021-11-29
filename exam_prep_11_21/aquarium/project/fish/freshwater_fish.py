from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    def __init__(self, name, species, price):
        super().__init__(name, species, size=3, price=price)

    def eat(self):
        self.size += 3
