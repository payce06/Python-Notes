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