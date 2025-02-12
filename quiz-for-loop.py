# 1. Function to reverse a string using a for loop
def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

print(reverse_string("hello"))  # Output: "olleh"

# 2. Function to iterate through numbers from 1 to 100 and print "Fizz", "Buzz", or "FizzBuzz"
def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizz_buzz()  # Prints Fizz, Buzz, or FizzBuzz for numbers 1 to 100


# 3. Function to find the sum of all numbers in an array using a for loop
def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total

print(sum_array([1, 2, 3, 4, 5]))  # Output: 15

# 4. Function to print the first n Fibonacci numbers using a for loop
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# 5. Function to calculate the factorial of a number using a for loop
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))  # Output: 120


# 6. Function that counts the number of occurrences of a specific character in a string using a for loop
def count_character(s, char):
    count = 0
    for c in s:
        if c == char:
            count += 1
    return count

print(count_character("hello world", "o"))  # Output: 2

# 7. Function to find the smallest number in an array using a for loop
def find_smallest(arr):
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest

print(find_smallest([3, 1, 4, 1, 5, 9]))  # Output: 1


# 8. Function that multiplies all the numbers in an array using a for loop
def multiply_array(arr):
    product = 1
    for num in arr:
        product *= num
    return product

print(multiply_array([1, 2, 3, 4]))  # Output: 24

# 9. Function that prints all prime numbers up to n using a for loop
def print_primes(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

print(print_primes(20))  # Output: [2, 3, 5, 7, 11, 13, 17, 19]


# 10. Function to reverse the elements of an array using a for loop
def reverse_array(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

print(reverse_array([1, 2, 3, 4, 5]))  # Output: [5, 4, 3, 2, 1]

# 11. Function that concatenates all strings in an array using a for loop
def concatenate_strings(arr):
    result = ""
    for string in arr:
        result += string
    return result

print(concatenate_strings(["Hello", " ", "world", "!"]))  # Output: "Hello world!"

# 12. Function to check if an array is sorted in ascending order using a for loop
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

print(is_sorted([1, 2, 3, 4, 5]))  # Output: True
print(is_sorted([1, 3, 2, 4, 5]))  # Output: False


# 13. Function to find the length of the longest word in a string using a for loop
def longest_word_length(s):
    words = s.split()
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
    return max_length

print(longest_word_length("The quick brown fox jumps over the lazy dog"))  # Output: 5

# 14. Function that finds the average of an array of numbers using a for loop
def average_array(arr):
    total = 0
    for num in arr:
        total += num
    return total / len(arr) if len(arr) > 0 else 0

print(average_array([1, 2, 3, 4, 5]))  # Output: 3.0

# 15. Function to create a new array that contains every second element of an existing array using a for loop
def every_second_element(arr):
    result = []
    for i in range(1, len(arr), 2):
        result.append(arr[i])
    return result

print(every_second_element([1, 2, 3, 4, 5, 6]))  # Output: [2, 4, 6]

# 16. Function to find the second largest number in an array using a for loop
def second_largest(arr):
    largest = second = float('-inf')
    for num in arr:
        if num > largest:
            second, largest = largest, num
        elif num > second and num < largest:
            second = num
    return second

print(second_largest([10, 20, 4, 45, 99]))  # Output: 45

# 17. Function that merges two arrays into one using a for loop
def merge_arrays(arr1, arr2):
    result = []
    for item in arr1:
        result.append(item)
    for item in arr2:
        result.append(item)
    return result

print(merge_arrays([1, 2, 3], [4, 5, 6]))  # Output: [1, 2, 3, 4, 5, 6]


# 18. Function to calculate the power of a number using a for loop
def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

print(power(2, 3))  # Output: 8

# 19. Function that counts how many even numbers are in an array using a for loop
def count_evens(arr):
    count = 0
    for num in arr:
        if num % 2 == 0:
            count += 1
    return count

print(count_evens([1, 2, 3, 4, 5, 6]))  # Output: 3

# 20. Function that finds the common elements between two arrays using a for loop
def common_elements(arr1, arr2):
    result = []
    for item in arr1:
        if item in arr2 and item not in result:
            result.append(item)
    return result

print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))  # Output: [3, 4]