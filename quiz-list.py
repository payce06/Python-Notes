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