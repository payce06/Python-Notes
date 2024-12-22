# 1. Write a function to find the length of an array without using the len() function.
def findLength(array):
    count = 0
    for item in array:
        count += 1
    return count

# Example
print(findLength([1, 2, 3, 4]))  # Output: 4
