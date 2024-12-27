import random

# MenuItem class
class MenuItem:
    def __init__(self, name, item_id, category, price):
        """Initialize the MenuItem object."""
        self.name = name
        self.item_id = item_id
        self.category = category
        self.price = price

    def __str__(self):
        return f"Name: {self.name}, Category: {self.category}, Price: ${self.price}"

# Employee class
class Employee:
    def __init__(self, name, employee_id, position):