# From float to int
pi = 3.14
int_pi = int(pi)  # Result: 3

# From string to int
num_str = "42"
num = int(num_str)  # Result: 42

# Invalid conversion
invalid_str = "abc"
# int(invalid_str)  # Raises ValueError

print(int_pi, num)

# From int to float
x = 10
float_x = float(x)  # Result: 10.0

# From string to float
num_str = "3.14"
pi = float(num_str)  # Result: 3.14
print(float_x, pi)

# From int/float to string
x = 10
pi = 3.14
str_x = str(x)  # Result: "10"
str_pi = str(pi)  # Result: "3.14"

# From boolean to string
is_ready = True
str_bool = str(is_ready)  # Result: "True"

print(str_x, str_pi, str_bool)

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