from employee import Employee, Developer, Manager
from hr_system import HRSystem


dev1 = Developer("Ahmed", "Ali", 7000, "Python")
dev2 = Developer("Sara", "Hassan", 6500, "JavaScript")

manager = Manager("Laila", "Khaled", 9000, [dev1])


hr = HRSystem()
hr.add_employee(dev1)
hr.add_employee(dev2)
hr.add_employee(manager)


print("All Employees:")
for emp in hr.list_employees():
    print(emp)


print("\nManager Team:")
for name in manager.list_employees():
    print(name)


dev1.apply_raise()
manager.apply_raise()

print("\nAfter Raise:")
print(dev1)
print(manager)


print("\nTotal Salary:")
print(hr.total_salary())
