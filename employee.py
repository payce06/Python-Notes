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