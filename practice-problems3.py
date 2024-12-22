# 1. Write a function to find the length of an array without using the len() function.
def findLength(array):
    count = 0
    for item in array:
        count += 1
    return count

# Example
print(findLength([1, 2, 3, 4]))  # Output: 4


# 2. Write a function to find the sum of all elements in an array.
def sumOfElements(array):
    total = 0
    for num in array:
        total += num
    return total

# Example
print(sumOfElements([1, 2, 3, 4]))  # Output: 10
