# Base class for an Employee
class Employee:
    def __init__(self, first_name, last_name, age, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.salary = salary
   
    # Method to get full name
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    # Method to display employee details

    def display_employee_info(self):
        print(f"Employee: {self.get_full_name()}")
        print(f"Age: {self.age}")
        print(f"Salary: ${self.salary}")
   
    # Method to increase salary
    def increase_salary(self, amount):
        self.salary += amount
        print(f"Salary of {self.get_full_name()} increased by ${amount}. New Salary: ${self.salary}")

# Manager class inherits from Employee
class Manager(Employee):
    def __init__(self, first_name, last_name, age, salary, department):
        super().__init__(first_name, last_name, age, salary)
self.department = department
        self.employees = []

    # Add employee to manager's list of employees
    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self.employees.append(employee)
            print(f"{employee.get_full_name()} added to {self.get_full_name()}'s team.")
        else:
            print("Only employees can be added.")
   
    # Display manager's team
    def display_team(self):
        print(f"{self.get_full_name()}'s Team:")
for employee in self.employees:
            employee.display_employee_info()

    # Override method to display manager details
    def display_employee_info(self):
        super().display_employee_info()
        print(f"Department: {self.department}")

# Department class
class Department:
    def __init__(self, name):
        self.name = name
        self.managers = []
   