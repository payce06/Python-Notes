# 1. Write a function to add two numbers.
def addNumbers(a, b):
    return a + b

# Example
print(addNumbers(3, 5))  # Output: 8

# 2. Write a function to check if a number is even or odd.
def isEvenOrOdd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example
print(isEvenOrOdd(7))  # Output: Odd

# 3. Write a function to find the factorial of a number.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
