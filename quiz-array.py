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


# 4. Function to sort an array of strings in alphabetical order
def sort_strings(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

print(sort_strings(["banana", "apple", "cherry"]))  # Output: ['apple', 'banana', 'cherry']

# 5. Function that returns the last element of an array
def last_element(arr):
    return arr[-1] if arr else None

print(last_element([1, 2, 3, 4]))  # Output: 4

# 6. Function to find the median of an array of numbers
def find_median(arr):
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_arr[mid - 1] + sorted_arr[mid]) / 2
    else:
        return sorted_arr[mid]

print(find_median([1, 3, 3, 6, 7, 8, 9]))  # Output: 6


# 7. Function that checks if an array contains a specific value
def contains_value(arr, value):
    for item in arr:
        if item == value:
            return True
    return False

print(contains_value([1, 2, 3, 4], 3))  # Output: True

# 8. Function to flatten a nested array (array of arrays)
def flatten_array(nested_arr):
    flat = []
    for sublist in nested_arr:
        for item in sublist:
            flat.append(item)
    return flat

print(flatten_array([[1, 2], [3, 4], [5]]))  # Output: [1, 2, 3, 4, 5]


# 9. Function that shuffles the elements of an array
import random
def shuffle_array(arr):
    shuffled = arr[:]
    random.shuffle(shuffled)
    return shuffled

print(shuffle_array([1, 2, 3, 4]))  # Output: Random order of [1, 2, 3, 4]

# 10. Function to rotate the elements of an array to the right by k steps
def rotate_array(arr, k):
    n = len(arr)
    k %= n
    return arr[-k:] + arr[:-k]

print(rotate_array([1, 2, 3, 4, 5], 2))  # Output: [4, 5, 1, 2, 3]

# 11. Function to split an array into chunks of a specific size
def chunk_array(arr, size):
    chunks = []
    for i in range(0, len(arr), size):
        chunks.append(arr[i:i + size])
    return chunks

print(chunk_array([1, 2, 3, 4, 5], 2))  # Output: [[1, 2], [3, 4], [5]]


# 12. Function that takes an array and a number and returns a new array with elements greater than the given number
def filter_greater(arr, num):
    result = []
    for item in arr:
        if item > num:
            result.append(item)
    return result

print(filter_greater([1, 2, 3, 4, 5], 3))  # Output: [4, 5]

# 13. Function to remove falsy values from an array
def remove_falsy(arr):
    result = []
    for item in arr:
        if item:
            result.append(item)
    return result

print(remove_falsy([0, 1, False, 2, "", 3, None]))  # Output: [1, 2, 3]


# 14. Function that finds the intersection of two arrays
def intersection(arr1, arr2):
    result = []
    for item in arr1:
        if item in arr2 and item not in result:
            result.append(item)
    return result

print(intersection([1, 2, 3], [2, 3, 4]))  # Output: [2, 3]

# 15. Function to find the difference between two arrays
def difference(arr1, arr2):
    result = []
    for item in arr1:
        if item not in arr2:
            result.append(item)
    for item in arr2:
        if item not in arr1:
            result.append(item)
    return result

print(difference([1, 2, 3], [2, 3, 4]))  # Output: [1, 4]

# 16. Function to concatenate two arrays
def concatenate_arrays(arr1, arr2):
    result = []
    for item in arr1:
        result.append(item)
    for item in arr2:
        result.append(item)
    return result

print(concatenate_arrays([1, 2], [3, 4]))  # Output: [1, 2, 3, 4]

# 17. Function that returns the first n elements of an array
def first_n_elements(arr, n):
    return arr[:n]

print(first_n_elements([1, 2, 3, 4, 5], 3))  # Output: [1, 2, 3]

# 18. Function to find the common elements in three arrays
def common_in_three(arr1, arr2, arr3):
    result = []
    for item in arr1:
        if item in arr2 and item in arr3 and item not in result:
            result.append(item)
    return result

print(common_in_three([1, 2, 3], [2, 3, 4], [3, 4, 5]))  # Output: [3]