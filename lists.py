# 1. Basic List Operations
print("BasicListOperations:")
myList = [1, 2, 3, "Apple", "Banana"]
print("originalList:", myList)

# Access Elements
print("firstElement:", myList[0])  # 1

# Append Elements
myList.append("Cherry")
print("afterAppend:", myList)  # [1, 2, 3, "Apple", "Banana", "Cherry"]

# Remove Elements
myList.remove(3)
print("afterRemove(3):", myList)  # [1, 2, "Apple", "Banana", "Cherry"]

# Length of List
print("lengthOfList:", len(myList))  # 5
print()
