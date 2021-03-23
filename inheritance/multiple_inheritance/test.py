from OOP.inheritance.multiple_inheritance.employee import Employee
from OOP.inheritance.multiple_inheritance.person import Person
from OOP.inheritance.multiple_inheritance.teacher import Teacher

teacher = Teacher()
person = Person()
print(person.sleep())
print(teacher.teach())
print(teacher.sleep())
print(teacher.get_fired())


