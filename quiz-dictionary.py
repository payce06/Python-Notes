# 1. Basic Dictionary Operations
# Question: How do you perform basic operations like accessing, adding, updating, and removing elements in a dictionary in Python?
def basic_dict_operations():
    print("Basic Dictionary Operations:")
    myDict = {"name": "John", "age": 25, "city": "New York"}
    print("originalDictionary:", myDict)

    # Access Elements
    print("name:", myDict["name"])  # "John"

    # Add/Update Elements
    myDict["age"] = 26  # Update age
    myDict["country"] = "USA"  # Add new key-value pair
    print("afterUpdate:", myDict)

    # Remove Elements
    del myDict["city"]  # Remove key "city"
    print("afterRemove(city):", myDict)

    # Check Key Existence
    print("hasKey('name'):", "name" in myDict)  # True
basic_dict_operations()
print()

# 2. Common Dictionary Methods
# Question: What are some common dictionary methods in Python for accessing keys, values, items, and removing elements?
def common_dict_methods():
    print("Common Dictionary Methods:")
    person = {"name": "Alice", "age": 30, "city": "Paris"}

    # Get Keys, Values, and Items
    print("keys:", person.keys())  # dict_keys(["name", "age", "city"])
    print("values:", person.values())  # dict_values(["Alice", 30, "Paris"])
    print("items:", person.items())  # dict_items([("name", "Alice"), ...])

    # Get with Default Value
    print("get(city):", person.get("city", "Not Found"))  # "Paris"
    print("get(country):", person.get("country", "Not Found"))  # "Not Found"

    # Pop and Popitem
    age = person.pop("age")
    print("afterPop(age):", person, "| poppedValue:", age)  # {"name": "Alice", "city": "Paris"}
    lastItem = person.popitem()  # Removes and returns the last key-value pair
    print("afterPopitem:", person, "| poppedItem:", lastItem)
common_dict_methods()
print()