from project.drink.drink import Drink


class Water(Drink):
    def __init__(self, name, portion, brand):
        super().__init__(name, portion, price=1.50, brand=brand)
