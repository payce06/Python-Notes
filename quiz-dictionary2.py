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

# 4. Function to check if an object contains a specific property
def contains_property(obj, prop):
    for key in obj:
        if key == prop:
            return True
    return False

print(contains_property({"a": 1, "b": 2}, "b"))  # Output: True

# 5. Function to deep clone an object
import copy
def deep_clone(obj):
    return copy.deepcopy(obj)

original = {"a": 1, "b": {"c": 2}}
clone = deep_clone(original)
print(clone)  # Output: {'a': 1, 'b': {'c': 2}}

# 6. Function to get the keys of an object
def get_keys(obj):
    keys = []
    for key in obj:
        keys.append(key)
    return keys

print(get_keys({"a": 1, "b": 2}))  # Output: ['a', 'b']


# 7. Function to get the values of an object
def get_values(obj):
    values = []
    for key in obj:
        values.append(obj[key])
    return values

print(get_values({"a": 1, "b": 2}))  # Output: [1, 2]

# 8. Function to invert the keys and values of an object
def invert_object(obj):
    inverted = {}
    for key, value in obj.items():
        inverted[value] = key
    return inverted

print(invert_object({"a": 1, "b": 2}))  # Output: {1: 'a', 2: 'b'}

# 9. Function that adds a property to an object
def add_property(obj, key, value):
    obj[key] = value
    return obj

print(add_property({"a": 1}, "b", 2))  # Output: {'a': 1, 'b': 2}

# 10. Function that deletes a property from an object
def delete_property(obj, key):
    if key in obj:
        del obj[key]
    return obj

print(delete_property({"a": 1, "b": 2}, "b"))  # Output: {'a': 1}
