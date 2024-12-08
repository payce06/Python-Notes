# 1. Iterating over a list
fruits = ["apple", "banana", "cherry"]
print("Iterating over a list:")
for fruit in fruits:
    print(fruit)
print()

# 2. Iterating over a tuple
colors = ("red", "green", "blue")
print("Iterating over a tuple:")
for color in colors:
    print(color)
print()

# 3. Iterating over a string
word = "Python"
print("Iterating over a string:")
for char in word:
    print(char)
print()

# 4. Iterating over a dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}
print("Iterating over a dictionary:")
for key, value in person.items():
    print(f"{key}: {value}")
print()

# 5. Using range()

# Requires Start, End, Step
# Quick Thing: For loop never reaches the End

print("Using range:")
# If you just specify one number, that is End
for i in range(5):  # 0 to 4
    print(i)

print("Range with start and stop:")

# If you just specify two numbers, that is Start, End
for i in range(1, 6):  # 1 to 5. We should not
    print(i)

print("Range with step:")
# If you specify three numbers, that is Start, End, Step
for i in range(0, 10, 2):  # Even numbers from 0 to 8 (because we should not include 10)
    print(i)
print()

# 6. Nested for loops
print("Nested for loops:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i}, {j})")
print()

# 7. Using break and continue
print("Using break:")
for i in range(1, 6):
    if i == 3:
        print("Breaking at 3")
        break
    print(i)

print("\nUsing continue:")
for i in range(1, 6):
    if i == 3:
        print("Skipping 3")
        continue
    print(i)
print()