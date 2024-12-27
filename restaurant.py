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
        """Initialize the Employee object."""
        self.name = name
        self.employee_id = employee_id
        self.position = position

    def display_info(self):
        """Display the employee's information."""
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")

# Customer class
class Customer:
    def __init__(self, name, customer_id):
        """Initialize the Customer object."""
        self.name = name
        self.customer_id = customer_id
        self.orders = []
        def place_order(self, menu_item):
        """Place an order for a menu item."""
        self.orders.append(menu_item)
        print(f"{self.name} has placed an order for {menu_item.name}.")

    def view_orders(self):
        """View all orders placed by the customer."""
        print(f"{self.name}'s Orders:")
        for order in self.orders:
            print(f"- {order.name} (${order.price})")

# Restaurant class
class Restaurant:
    def __init__(self, name):
        """Initialize the Restaurant object."""
        self.name = name
        self.menu = []
        self.employees = []
        self.customers = []

    def add_menu_item(self, menu_item):
        """Add a menu item to the restaurant's menu."""
    
        self.menu.append(menu_item)
        print(f"Added {menu_item.name} to the menu.")

    def remove_menu_item(self, menu_item):
        """Remove a menu item from the restaurant's menu."""
        if menu_item in self.menu:
            self.menu.remove(menu_item)
            print(f"Removed {menu_item.name} from the menu.")
        else:
            print(f"{menu_item.name} not found in the menu.")

    def register_employee(self, employee):
        """Register an employee in the restaurant."""
        self.employees.append(employee)
        print(f"Employee {employee.name} has been registered.")

    def register_customer(self, customer):
        """Register a customer in the restaurant."""
        self.customers.append(customer)
    
    print(f"Customer {customer.name} has been registered.")

    def display_menu(self):
        """Display the restaurant's menu."""
        print("\nRestaurant Menu:")
        for item in self.menu:
            print(item)

    def display_employees(self):
        """Display all employees in the restaurant."""
        print("\nRestaurant Employees:")
        for employee in self.employees:
            employee.display_info()

    def display_customers(self):
        """Display all customers in the restaurant."""
        print("\nRestaurant Customers:")
        for customer in self.customers:
            print(f"- {customer.name}")