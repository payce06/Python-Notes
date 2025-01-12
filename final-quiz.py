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