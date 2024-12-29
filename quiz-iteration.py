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