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

# 2. Set Operations
print("SetOperations:")
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}

# Union
print("union:", setA.union(setB))  # {1, 2, 3, 4, 5, 6}

# Intersection
print("intersection:", setA.intersection(setB))  # {3, 4}

# Difference
print("difference(A-B):", setA.difference(setB))  # {1, 2}
print("difference(B-A):", setB.difference(setA))  # {5, 6}

# 3. Common Set Methods
print("CommonSetMethods:")
numbers = {1, 2, 3}

# Add and Discard
numbers.add(4)
print("afterAdd(4):", numbers)  # {1, 2, 3, 4}
numbers.discard(2)
print("afterDiscard(2):", numbers)  # {1, 3, 4}

# Pop
popped = numbers.pop()  # Removes a random element
print("afterPop:", numbers, "| poppedElement:", popped)

# Clear
numbers.clear()
print("afterClear:", numbers)  # set()
print()

# 4. Iterating Over Sets
print("IteratingOverSets:")
fruits = {"Apple", "Banana", "Cherry"}
for fruit in fruits:
    print(fruit)