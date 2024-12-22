# 1. Basic Set Operations
print("BasicSetOperations:")
mySet = {1, 2, 3, "Apple", "Banana"}
print("originalSet:", mySet)

# Add Elements
mySet.add("Cherry")
print("afterAdd(Cherry):", mySet)

# Remove Elements
mySet.remove(3)
print("afterRemove(3):", mySet)

# Check Membership
print("contains(Apple):", "Apple" in mySet)  # True
print("contains(Orange):", "Orange" in mySet)  # False

# Set Length
print("lengthOfSet:", len(mySet))  # Number of elements in the set
print()