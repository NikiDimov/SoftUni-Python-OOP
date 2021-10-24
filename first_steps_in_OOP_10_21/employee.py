class Employee:
    def __init__(self, id, first_name, last_name, salary):
        self.id, self.first_name, self.last_name, self.salary = id, first_name, last_name, salary

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_annual_salary(self):
        return 12 * self.salary

    def raise_salary(self, amount):
        self.salary += amount
        return self.salary


employee = Employee(744423129, "John", "Smith", 1000)
print(employee.get_full_name())
print(employee.raise_salary(500))
print(employee.get_annual_salary())
