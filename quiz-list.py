# 1. Basic List Operations
# Question: How do you perform basic operations like accessing, appending, and removing elements in a list in Python?
def basic_list_operations():
    print("Basic List Operations:")
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
basic_list_operations()
print()

# 2. Slicing And Indexing
# Question: How can you slice and index a list in Python?
def slicing_and_indexing():
    print("Slicing And Indexing:")
    nums = [0, 1, 2, 3, 4, 5]
    print("originalList:", nums)
    print("firstThreeElements:", nums[:3])  # [0, 1, 2]
    print("lastTwoElements:", nums[-2:])  # [4, 5]
    print("reversedList:", nums[::-1])  # [5, 4, 3, 2, 1, 0]
slicing_and_indexing()
print()

# 3. Common List Methods
# Question: What are some common list methods in Python for modifying a list (like append, extend, insert, remove, pop, etc.)?
def common_list_methods():
    print("Common List Methods:")
    numbers = [4, 2, 8, 6, 2]

    # Append and Extend
    numbers.append(10)
    print("afterAppend:", numbers)  # [4, 2, 8, 6, 2, 10]
    numbers.extend([20, 30])
    print("afterExtend:", numbers)  # [4, 2, 8, 6, 2, 10, 20, 30]

    # Insert
    numbers.insert(1, 99)
    print("afterInsert:", numbers)  # [4, 99, 2, ...]

    # Remove and Pop
    numbers.remove(2)
    print("afterRemove(2):", numbers)
    last = numbers.pop()
    print("afterPop:", numbers, "| poppedElement:", last)

    
    # Sort and Reverse
    numbers.sort()
    print("afterSort:", numbers)  # [4, 6, 8, ...]
    numbers.reverse()
    print("afterReverse:", numbers)  # [..., 8, 6, 4]
common_list_methods()
print()

# 4. Iterating Over Lists
# Question: How do you iterate over a list in Python and access the index of each element?
def iterating_over_lists():
    print("Iterating Over Lists:")
    fruits = ["Apple", "Banana", "Cherry"]
    for fruit in fruits:
        print(fruit)

    # Using Enumerate
    for index, fruit in enumerate(fruits):
        print(f"index {index}: {fruit}")
iterating_over_lists()
print()
