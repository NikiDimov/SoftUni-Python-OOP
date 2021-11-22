from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '' or value == ' ':
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type, name, price):
        for food in self.food_menu:
            if food.name == name:
                raise Exception(f"{food_type} {name} is already in the menu!")
        if food_type == "Bread":
            self.food_menu.append(Bread(name, price))
        elif food_type == "Cake":
            self.food_menu.append(Cake(name, price))
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type, name, portion, brand):
        for drink in self.drinks_menu:
            if drink.name == name:
                raise Exception(f"{drink_type} {name} is already in the menu!")
        if drink_type == "Tea":
            self.drinks_menu.append(Tea(name, portion, brand))
        elif drink_type == "Water":
            self.drinks_menu.append(Water(name, portion, brand))
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type, table_number, capacity):
        for table in self.tables_repository:
            if table.table_number == table_number:
                raise Exception(f"Table {table_number} is already in the bakery!")
        if table_type == "InsideTable":
            self.tables_repository.append(InsideTable(table_number, capacity))
        elif table_type == "OutsideTable":
            self.tables_repository.append(OutsideTable(table_number, capacity))
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def checker(self, table_number, menu, *args):
        products_not_in_the_menu = []
        result = ''
        for table in self.tables_repository:
            if table.table_number == table_number:
                result += f"Table {table_number} ordered:\n"
                for product_name in args:
                    product_in_the_menu = False
                    for product in menu:
                        if product.name == product_name:
                            product_in_the_menu = True
                            if product.__class__.__bases__[0].__name__ == "BakedFood":
                                table.order_food(product)
                            elif product.__class__.__bases__[0].__name__ == "Drink":
                                table.order_drink(product)
                            self.total_income += product.price
                            result += f"{product}\n"
                            break
                    if not product_in_the_menu:
                        products_not_in_the_menu.append(product_name)
                result += f"{self.name} does not have in the menu:\n"
                for product in products_not_in_the_menu:
                    result += f"{product}\n"
                return result
        return f"Could not find table {table_number}\n"

    def order_food(self, table_number, *food_names):
        return self.checker(table_number, self.food_menu, *food_names)

    def order_drink(self, table_number, *drink_names):
        return self.checker(table_number, self.drinks_menu, *drink_names)

    def leave_table(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                bill = table.get_bill()
                table.clear()
                return f"Table: {table_number}\nBill: {bill:.2f}"

    def get_free_tables_info(self):
        result = ''
        for table in self.tables_repository:
            if not table.is_reserved:
                result += f"{table.free_table_info()}\n"
        return result

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

# bakery = Bakery("Pri Niko")
# bakery.add_table("InsideTable", 5, 10)
# bakery.add_food("Bread", "Corny", 2)
# bakery.add_food("Cake", "Sweet", 1)
# bakery.reserve_table(3)
# print(bakery.order_food(5, "Corny", "Sweet"))
# print(bakery.leave_table(5))
# print(bakery.get_free_tables_info())
