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