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

# Example
print(factorial(5))  # Output: 120

# 4. Write a function to check if a string is a palindrome.
def isPalindrome(string):
    return string == string[::-1]

# Example
print(isPalindrome("radar"))  # Output: True

# 5. Write a function to calculate the nth Fibonacci number.
def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
