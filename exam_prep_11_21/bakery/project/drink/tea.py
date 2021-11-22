from project.drink.drink import Drink


class Tea(Drink):
    def __init__(self, name, portion, brand):
        super().__init__(name, portion, price=2.50, brand=brand)
