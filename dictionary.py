# 1. Basic Dictionary Operations
print("BasicDictionaryOperations:")
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
print()

# 2. Common Dictionary Methods
print("CommonDictionaryMethods:")
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
print()

# 3. Iterating Over Dictionaries
print("IteratingOverDictionaries:")
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
print()

# 4. Nested Dictionaries
print("NestedDictionaries:")
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
print()