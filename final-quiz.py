# Question 1: Check if a number is a palindrome
def is_palindrome(num):
    """
    Write a Python function to check whether a given number is a palindrome.
    """
    num_str = str(num)
    reversed_num = ""
    for i in range(len(num_str) - 1, -1, -1):
        reversed_num += num_str[i]
    return num_str == reversed_num

print(is_palindrome(121))  # True
print(is_palindrome(123))  # False

# Question 2: Find factorial using recursion
def factorial(n):
    """
    Write a Python program to find the factorial of a number using recursion.
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))  # 120

# Question 3: Sum of all even numbers in a list
def sum_even_numbers(numbers):
    """
    Write a Python function that takes a list of numbers and returns the sum of all even numbers.
    """
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

print(sum_even_numbers([1, 2, 3, 4, 5, 6]))  # 12

# Question 4: Count vowels in a string
def count_vowels(s):
    """
    Write a Python program that takes a string and returns the number of vowels in it.
    """
    count = 0
    for char in s:
        if char.lower() in 'aeiou':
            count += 1
    return count

print(count_vowels("Hello World"))  # 3


# Question 5: Reverse a list without using slicing
def reverse_list(lst):
    """
    Write a Python function to reverse a list without using slicing (ie a[::-1].
    """
    reversed_lst = []
    for item in lst:
        # Insert the current element at 0 index
        reversed_lst.insert(0, item)
    return reversed_lst

print(reverse_list([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]

# Question 6: Find the largest number in a list
def find_largest(numbers):
    """
    Write a Python function that finds the largest number in a given list.
    """
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

print(find_largest([1, 2, 3, 4, 5]))  # 5

# Question 7: Merge two dictionaries
def merge_dicts(dict1, dict2):
    """
    Write a Python program that merges two dictionaries into one.
    """
    merged = {}
    for key, value in dict1.items():
        merged[key] = value
    for key, value in dict2.items():
        merged[key] = value
    return merged

print(merge_dicts({"a": 1, "b": 2}, {"c": 3, "d": 4}))  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Question 8: Check if a number is prime
def is_prime(n):
    """
    Write a Python function to check if a number is prime.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))  # True
print(is_prime(10))  # False

# Question 9: Fibonacci sequence
def fibonacci(n):
    """
    Write a Python program that prints the Fibonacci sequence up to a given number.
    """
    fib = [0, 1]
    for i in range(2, n):
        next_fib = fib[-1] + fib[-2]
        fib.append(next_fib)
    return fib

print(fibonacci(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# Question 10: Find the average of numbers in a list
def average(numbers):
    """
    Write a Python function that takes a list of numbers and returns the average of the numbers.
    """
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers) if numbers else 0

print(average([1, 2, 3, 4, 5]))  # 3.0

# Question 11: Remove duplicates from a list
def remove_duplicates(numbers):
    """
    Write a Python program that removes duplicates from a list.
    """
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers

print(remove_duplicates([1, 2, 2, 3, 4, 4]))  # [1, 2, 3, 4]

# Question 12: Find intersection of two lists
def list_intersection(list1, list2):
    """
    Write a Python function to find the intersection of two lists.
    """
    intersection = []
    for item in list1:
        if item in list2 and item not in intersection:
            intersection.append(item)
    return intersection

print(list_intersection([1, 2, 3], [3, 4, 5]))  # [3]


# Question 13: Check if a word is an anagram
def is_anagram(word1, word2):
    """
    Write a Python program that checks if a word is an anagram of another word.
    Eg: abc and acb are anagrams as one can be formed by arranging the letters in another.
    """
    if len(word1) != len(word2):
        return False
    for char in word1:
        if word1.count(char) != word2.count(char):
            return False
    return True

print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))  # False

# Question 14: Reverse a string without slicing
def reverse_string(s):
    """
    Write a Python program to reverse a string without using slicing.
    """
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

print(reverse_string("hello"))  # "olleh"

# Question 15: Find the second largest number in a list
def second_largest(numbers):
    """
    Write a Python function to find the second largest number in a list.
    """
    largest = second = float('-inf')
    for num in numbers:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    return second

print(second_largest([1, 2, 3, 4, 5]))  # 4

# Question 16: Celsius to Fahrenheit conversion
def celsius_to_fahrenheit(celsius):
    """
    Write a Python program that converts a given temperature in Celsius to Fahrenheit.
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

print(celsius_to_fahrenheit(0))  # 32
print(celsius_to_fahrenheit(100))  # 212

# Question 17: Count characters excluding spaces
def count_chars_excluding_spaces(s):
    """
    Write a Python program that counts the number of characters in a string, excluding spaces.
    """
    count = 0
    for char in s:
        if char != ' ':
            count += 1
    return count

print(count_chars_excluding_spaces("Hello World"))  # 10