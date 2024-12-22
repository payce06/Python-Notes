# 1. Write a function to check if a number is positive, negative, or zero.
def checkNumber(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Example
print(checkNumber(-5))  # Output: Negative

# 2. Write a function to find the largest of three numbers.
def findLargestOfThree(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

# Example
print(findLargestOfThree(3, 7, 5))  # Output: 7

# 3. Write a function to determine if a year is a leap year.
def isLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Example
print(isLeapYear(2024))  # Output: True

# 4. Write a function to find the sum of all numbers in a list using a for loop.
def sumOfList(numbers):
    total = 0
    for num in numbers:
        total += num
    return total