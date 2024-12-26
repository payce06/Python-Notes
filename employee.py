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