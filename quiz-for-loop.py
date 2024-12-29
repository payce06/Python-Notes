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