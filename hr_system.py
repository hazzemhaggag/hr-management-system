class HRSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def list_employees(self):
        return [str(emp) for emp in self.employees]

    def total_salary(self):
        return sum(emp.salary for emp in self.employees)
