# 1. Basic Tuple Operations
print("BasicTupleOperations:")
myTuple = (1, 2, 3, "Apple", "Banana")
print("originalTuple:", myTuple)

# Access Elements
print("firstElement:", myTuple[0])  # 1

# Tuples are immutable, no append or remove
print("immutableNote: Tuples cannot be modified (no append/remove).")
print()

# 2. Slicing And Indexing
print("SlicingAndIndexing:")
nums = (0, 1, 2, 3, 4, 5)
print("originalTuple:", nums)
print("firstThreeElements:", nums[:3])  # Getting the first 3 values. (0, 1, 2)
print("lastTwoElements:", nums[-2:])  # Getting the last two values. (4, 5)
print("reversedTuple:", nums[::-1])  # Reversing a tuple. (5, 4, 3, 2, 1, 0)
print()

# 3. Tuple Methods
print("TupleMethods:")
numbers = (4, 2, 8, 6, 2)
print("originalTuple:", numbers)

# Count and Index
countOf2 = numbers.count(2)
print("countOf2:", countOf2)  # 2
indexOf8 = numbers.index(8)
print("indexOf8:", indexOf8)  # 2
print()

# 4. Iterating Over Tuples
print("IteratingOverTuples:")
fruits = ("Apple", "Banana", "Cherry")
for fruit in fruits:
    print(fruit)