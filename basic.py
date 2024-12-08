# From int to boolean
x = 0
bool_x = bool(x)  # Result: False

# From string to boolean
name = "Payce Grossman"
empty_str = ""
bool_name = bool(name)  # Result: True
bool_empty = bool(empty_str)  # Result: False

print(bool_x, bool_name, bool_empty)

# Take user input
user_input = input("Enter your name: ")
print("Hello, " + user_input)

# Basic input
name = input("What is your name? ")
print(f"Hello, {name}!")

# Integer input
age = int(input("Enter your age: "))
print(f"You are {age} years old.")

# Multiple inputs
# Single-line input
x, y, z = input("Enter three numbers separated by space: ").split()
print(f"x={x}, y={y}, z={z}")

# Output
name = "Payce"
age = 16
print(f"My name is {name} and I am {age} years old.")
print("My name is {} and I am {} years old.".format(name, age))
