# 1. Simple `if` statement
x = 10
if x > 5:
    print("x is greater than 5")

# 2. `if-else` statement
x = 3
if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")

# 3. `if-elif-else` statement
x = 15
if x < 10:
    print("x is less than 10")
elif x == 10:
    print("x is equal to 10")
else:
    print("x is greater than 10")

# 4. Nested conditions
x = 20
if x > 10:
    if x < 30:
        print("x is between 10 and 30")
    else:
        print("x is greater than or equal to 30")
else:
    print("x is less than or equal to 10")

    # 5. Using logical operators
age = 25
if age >= 18 and age <= 35:
    print("You are eligible for the program")
age = 70
if age < 18 or age > 60:
    print("You qualify for a discount")
logged_in = False
if not logged_in:
    print("Please log in")

# 6. Using `pass`
x = 10
if x > 5:
    pass  # Do nothing for now
else:
    print("x is not greater than 5")

# Practical examples

# 7. Check if a number is positive, negative, or zero
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")