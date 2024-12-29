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

# 3. Iterating Over Dictionaries
# Question: How do you iterate over a dictionary to access its keys, values, and key-value pairs in Python?
def iterating_over_dicts():
    print("Iterating Over Dictionaries:")
    fruits = {"apple": 3, "banana": 5, "cherry": 2}

    # Keys
    for key in fruits:
        print(f"key: {key}")

    # Values
    for value in fruits.values():
        print(f"value: {value}")

    # Key-Value Pairs
    for key, value in fruits.items():
        print(f"{key}: {value}")
iterating_over_dicts()
print()

# 4. Nested Dictionaries
# Question: How do you access and iterate over elements in a nested dictionary in Python?
def nested_dicts():
    print("Nested Dictionaries:")
    students = {
        "student1": {"name": "John", "age": 20},
        "student2": {"name": "Alice", "age": 22},
    }

    print("student1Name:", students["student1"]["name"])  # "John"

    # Iterating Over Nested Dictionary
    for student_id, details in students.items():
        print(f"{student_id}:")
        for key, value in details.items():
            print(f"  {key}: {value}")
nested_dicts()
print()