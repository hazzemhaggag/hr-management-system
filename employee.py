class Employee:
    raise_amount = 1.05

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary  

    # =====================
    # Property + Setter
    # =====================
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 3000:
            raise ValueError("Salary cannot be less than 3000")
        self._salary = value

    @property
    def fullname(self):
        return f"{self.first} {self.last}"


    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)



    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount


    @staticmethod
    def is_workday(day):
        return day.weekday() < 5



    def __str__(self):
        return f"{self.fullname} - {self.salary}"


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, salary, language):
        super().__init__(first, last, salary)
        self.language = language

    def __str__(self):
        return f"{self.fullname} - {self.salary} - {self.language}"


class Manager(Employee):
    def __init__(self, first, last, salary, employees=None):
        super().__init__(first, last, salary)
        self.employees = employees if employees else []

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def list_employees(self):
        return [emp.fullname for emp in self.employees]
