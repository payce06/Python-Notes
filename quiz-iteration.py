# 1. Iterating over a list
# Question: How can you iterate over a list in Python and print each item?
def iterate_list():
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(fruit)
iterate_list()
print()

# 2. Iterating over a tuple
# Question: How do you iterate over a tuple in Python and print each item?
def iterate_tuple():
    colors = ("red", "green", "blue")
    for color in colors:
        print(color)
iterate_tuple()
print()

# 3. Iterating over a string
# Question: How can you iterate over a string in Python and print each character?
def iterate_string():
    word = "Python"
    for char in word:
        print(char)
iterate_string()
print()

# 4. Iterating over a dictionary
# Question: How do you iterate over a dictionary in Python and print key-value pairs?
def iterate_dict():
    person = {"name": "Alice", "age": 30, "city": "New York"}
    for key, value in person.items():
        print(f"{key}: {value}")
iterate_dict()
print()

# 5. Using range()
# Question: How can you use the range function in a for loop in Python?
def range_example():
    print("Using range:")
    for i in range(5):  # 0 to 4
        print(i)
range_example()
print()

def range_with_start_end():
    print("Range with start and stop:")
    for i in range(1, 6):  # 1 to 5
        print(i)
range_with_start_end()
print()

def range_with_step():
    print("Range with step:")
    for i in range(0, 10, 2):  # Even numbers from 0 to 8
        print(i)
range_with_step()
print()

# 6. Nested for loops
# Question: How can you use nested for loops in Python to iterate over multiple ranges?
def nested_loops():
    print("Nested for loops:")
    for i in range(1, 4):
        for j in range(1, 4):
            print(f"({i}, {j})")
nested_loops()
print()

# 7. Using break and continue
# Question: How do you use break to exit a loop early in Python?
def break_example():
    print("Using break:")
    for i in range(1, 6):
        if i == 3:
            print("Breaking at 3")
            break
        print(i)
break_example()
print()