# 1. Function to merge two objects into one
def merge_objects(obj1, obj2):
    merged = {}
    for key, value in obj1.items():
        merged[key] = value
    for key, value in obj2.items():
        merged[key] = value
    return merged

print(merge_objects({"a": 1, "b": 2}, {"b": 3, "c": 4}))  # Output: {'a': 1, 'b': 3, 'c': 4}

# 2. Function to count the number of properties in an object
def count_properties(obj):
    count = 0
    for key in obj:
        count += 1
    return count

print(count_properties({"a": 1, "b": 2, "c": 3}))  # Output: 3

# 3. Function that takes an array of objects and returns an array of values for a specific property
def get_property_values(arr, prop):
    values = []
    for obj in arr:
        if prop in obj:
            values.append(obj[prop])
    return values

print(get_property_values([{"a": 1}, {"a": 2}, {"b": 3}], "a"))  # Output: [1, 2]