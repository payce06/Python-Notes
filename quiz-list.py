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