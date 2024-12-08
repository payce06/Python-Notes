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

# 5. Lambda Functions
square = lambda x: x**2
add = lambda a, b: a + b

print("Lambda Functions:")
print(f"Square of 4: {square(4)}")
print(f"Sum of 3 and 7: {add(3, 7)}")
print()

# 6. Nested Functions
def outer_function():
    print("Outer function")
   
    def inner_function():
        print("Inner function")
   
    inner_function()

print("Nested Functions:")
outer_function()
print()
