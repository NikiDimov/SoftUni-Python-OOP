from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name, salary_one, salary_two, *children):
        super().__init__(name=family_name, budget=salary_one + salary_two, members_count=2 + len(children))
        self.room_cost = 30
        self.children = list(children)
        self.appliances = [TV() for _ in range(self.members_count)] + \
                          [Fridge() for _ in range(self.members_count)] + \
                          [Laptop() for _ in range(self.members_count)]

        self.expenses = sum([el.get_monthly_expense() for el in self.appliances]) + \
                        30 * sum([el.cost for el in self.children])
