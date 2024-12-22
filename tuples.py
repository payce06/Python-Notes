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
