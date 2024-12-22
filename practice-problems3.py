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


# Example
print(secondLargest([4, 1, 3, 2, 4]))  # Output: 3

# 4. Write a function to remove duplicates from an array.
def removeDuplicates(array):
    uniqueArray = []
    for item in array:
        if item not in uniqueArray:
            uniqueArray.append(item)
    return uniqueArray

# Example
print(removeDuplicates([1, 2, 2, 3, 4, 4]))  # Output: [1, 2, 3, 4]


# 5. Write a function to reverse an array.
def reverseArray(array):
    reversedArray = []
    for i in range(len(array) - 1, -1, -1):
        reversedArray.append(array[i])
    return reversedArray

# Example
print(reverseArray([1, 2, 3, 4]))  # Output: [4, 3, 2, 1]

# 6. Write a function to find the intersection of two arrays.
def arrayIntersection(array1, array2):
    intersection = []
    for item1 in array1:
        for item2 in array2:
            if item1 == item2 and item1 not in intersection:
                intersection.append(item1)
    return intersection


# Example
print(arrayIntersection([1, 2, 3], [2, 3, 4]))  # Output: [2, 3]

# 7. Write a function to find the index of the first occurrence of an element in an array.
def findIndex(array, target):
    index = 0
    for element in array:
        if element == target:
            return index
        index += 1
    return -1  # Return -1 if the element is not found

# Example
print(findIndex([1, 2, 3, 4, 5], 3))  # Output: 2
print(findIndex([1, 2, 3, 4, 5], 6))  # Output: -1

# 8. Write a function to flatten a nested array.
def flattenArray(nestedArray):
    flatArray = []
    for item in nestedArray:
        if isinstance(item, list):
            subArray = flattenArray(item)
            for subItem in subArray:
                flatArray.append(subItem)
        else:
            flatArray.append(item)
    return flatArray

# Example
print(flattenArray([1, [2, [3, 4], 5]]))  # Output: [1, 2, 3, 4, 5]