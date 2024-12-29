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