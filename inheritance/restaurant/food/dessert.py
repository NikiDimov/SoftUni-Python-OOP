from OOP.inheritance.restaurant.food.food import Food


class Dessert(Food):
    def __init__(self, name, price, gram, calories):
        super().__init__(name, price, gram)
        self.__calories = calories

    @property
    def calories(self):
        return self.__calories

