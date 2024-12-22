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


# 3. Write a function to find the second largest element in an array.
def secondLargest(array):
    largest = None
    secondLargest = None
    for num in array:
        if largest is None or num > largest:
            secondLargest = largest
            largest = num
        elif secondLargest is None or (num > secondLargest and num != largest):
            secondLargest = num
    return secondLargest

