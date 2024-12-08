# 1. Basic Function Definition and Invocation
def greet():
    print("Hello, World!")

print("Basic Function:")
greet()  # Output: Hello, World!
print()

# 2. Function with Parameters and Return Value
def add(a, b):
    return a + b

print("Function with Parameters and Return Value:")
result = add(3, 5)
print(f"3 + 5 = {result}")
print()

# 3. Default Arguments
def introduce(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

print("Default Arguments:")
introduce("Alice")  # Uses default greeting
introduce("Bob", "Hi")  # Custom greeting
print()