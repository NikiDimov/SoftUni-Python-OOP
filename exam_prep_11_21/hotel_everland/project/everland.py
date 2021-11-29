class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        if room not in self.rooms:
            self.rooms.append(room)

    def get_monthly_consumptions(self):
        expenses = sum([room.expenses for room in self.rooms])
        room_cost = sum([room.room_cost for room in self.rooms])
        return f"Monthly consumption: {expenses + room_cost:.2f}$."

    def pay(self):
        result = ''
        for room in self.rooms:
            total_expenses = room.room_cost + room.expenses
            if room.budget >= total_expenses:
                room.budget -= total_expenses
                result += f"{room.family_name} paid {total_expenses:.2f}$ and have {room.budget:.2f} left.\n"
            else:
                result += f"{room.family_name} does not have enough budget and must leave the hotel.\n"
                self.rooms.remove(room)
        return result.strip()

    def status(self):
        result = ''
        population = sum([room.members_count for room in self.rooms])
        result += f"{population}\n"
        for room in self.rooms:
            result += f"{room.family_name} with {room.members_count}. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n"
            if room.__class__.__name__ == "YoungCoupleWithChildren":
                for child in room.children:
                    result += f"--- Child {room.children.index(child)+1} monthly cost: {child.cost * 30:.2f}$\n"
            cost_all_appliances = 0
            for appliance in room.appliances:
                cost_all_appliances += appliance.get_monthly_expense()
            result += f"--- Appliances monthly cost: {cost_all_appliances:.2f}$\n"
        return result.strip()





# from rooms.young_couple import YoungCouple
# from rooms.young_couple_with_children import YoungCoupleWithChildren
# from people.child import Child
#
#
# everland = Everland()
#
# def test_one():
#     young_couple = YoungCouple("Johnsons", 150, 205)
#
#     child1 = Child(5, 1, 2, 1)
#     child2 = Child(3, 2)
#     young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child1, child2)
#
#     everland.add_room(young_couple)
#     everland.add_room(young_couple_with_children)
#
#     print(everland.get_monthly_consumptions())
#     print(everland.pay())
#     print(everland.status())
#
#
# if __name__ == "__main__":
#     test_one()
