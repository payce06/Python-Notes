# 1. Function to find the maximum number in an array
def find_maximum(arr):
    maximum = arr[0]
    for num in arr:
        if num > maximum:
            maximum = num
    return maximum

print(find_maximum([3, 1, 4, 1, 5, 9]))  # Output: 9

# 2. Function to remove duplicates from an array
def remove_duplicates(arr):
    unique = []
    for item in arr:
        if item not in unique:
            unique.append(item)
    return unique

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]

# 3. Function that takes an array of numbers and returns a new array with each number squared
def square_elements(arr):
    squared = []
    for num in arr:
        squared.append(num ** 2)
    return squared

print(square_elements([1, 2, 3, 4]))  # Output: [1, 4, 9, 16]