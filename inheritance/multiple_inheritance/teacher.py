from OOP.inheritance.multiple_inheritance.employee import Employee
from OOP.inheritance.multiple_inheritance.person import Person


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."
