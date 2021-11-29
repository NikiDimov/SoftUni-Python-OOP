class Room:
    def __init__(self, name, budget, members_count):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        total_cost = 0
        for el in args:
            for instance in el:
                if instance.__class__.__name__ == "Child":
                    total_cost += instance.cost*30
                else:
                    total_cost += instance.get_monthly_expense()
        self.expenses = total_cost



