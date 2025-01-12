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