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
