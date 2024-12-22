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
# Example
print(fibonacci(7))  # Output: 8

# 6. Write a function to find the largest number in a list.
def findLargest(numbers):
    return max(numbers)

# Example
print(findLargest([1, 3, 7, 0, 5]))  # Output: 7

# 7. Write a function to reverse a string.
def reverseString(s):
    return s[::-1]

# Example
print(reverseString("hello"))  # Output: "olleh"

# 8. Write a function to count the number of vowels in a string.
def countVowels(string):
    vowels = "aeiouAEIOU"
    vowelCount = 0
    for ch in string:
        if ch in vowels:
            vowelCount += 1
    return vowelCount

# Example
print(countVowels("Python Programming"))  # Output: 4

# 9. Write a function to convert Celsius to Fahrenheit.
def celsiusToFahrenheit(celsius):
    return (celsius * 9/5) + 32

# Example
print(celsiusToFahrenheit(25))  # Output: 77.0

# 10. Write a function to find the GCD of two numbers.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example
print(gcd(48, 18))  # Output: 6