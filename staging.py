# If you just specify two numbers, that is Start, End
for i in range(1, 6):  # 1 to 5. We should not
    print(i)

print("Range with step:")
# If you specify three numbers, that is Start, End, Step
for i in range(0, 10, 2):  # Even numbers from 0 to 8 (because we should not include 10)
    print(i)
print()

# 6. Nested for loops
print("Nested for loops:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i}, {j})")
print()

# 7. Using break and continue
print("Using break:")
for i in range(1, 6):
    if i == 3:
        print("Breaking at 3")
        break
    print(i)

print("\nUsing continue:")
for i in range(1, 6):
    if i == 3:
        print("Skipping 3")
        continue
    print(i)
print()