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

# Example
print(sumOfList([1, 2, 3, 4, 5]))  # Output: 15

# 5. Write a function to print all even numbers in a range.
def evenNumbersInRange(start, end):
    evens = []
    for num in range(start, end + 1):
        if num % 2 == 0:
            evens.append(num)
    return evens

# Example
print(evenNumbersInRange(1, 10))  # Output: [2, 4, 6, 8, 10]

# 6. Write a function to count the occurrences of a specific element in a list.
def countOccurrences(numbers, target):
    count = 0
    for num in numbers:
        if num == target:
            count += 1
    return count

# Example
print(countOccurrences([1, 2, 2, 3, 4, 2], 2))  # Output: 3

# 7. Write a function to find the smallest number in a list using a for loop.
def findSmallest(numbers):
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest

# Example
print(findSmallest([3, 1, 4, 1, 5]))  # Output: 1

# 8. Write a function to print the multiplication table of a number.
def multiplicationTable(n):
    table = []
    for i in range(1, 11):
        table.append(f"{n} x {i} = {n * i}")
    return table

# Example
print("\n".join(multiplicationTable(5)))

# 9. Write a function to calculate the sum of all odd numbers in a range.
def sumOfOddNumbers(start, end):
    total = 0
    for num in range(start, end + 1):
        if num % 2 != 0:
            total += num
    return total

# Example
print(sumOfOddNumbers(1, 10))  # Output: 25

# 10. Write a function to check if a given number is prime.
def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Example
print(isPrime(17))  # Output: True