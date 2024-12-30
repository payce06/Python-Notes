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

# 11. Function to check if two objects are equal
def are_objects_equal(obj1, obj2):
    if len(obj1) != len(obj2):
        return False
    for key in obj1:
        if key not in obj2 or obj1[key] != obj2[key]:
            return False
    return True

print(are_objects_equal({"a": 1, "b": 2}, {"a": 1, "b": 2}))  # Output: True


# 12. Function that returns an array of key-value pairs from an object
def object_to_pairs(obj):
    pairs = []
    for key, value in obj.items():
        pairs.append((key, value))
    return pairs

print(object_to_pairs({"a": 1, "b": 2}))  # Output: [('a', 1), ('b', 2)]

# 13. Function to sort an array of objects by a specific property
def sort_objects(arr, prop):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i].get(prop, 0) > arr[j].get(prop, 0):
                arr[i], arr[j] = arr[j], arr[i]
    return arr

print(sort_objects([{"a": 3}, {"a": 1}, {"a": 2}], "a"))  # Output: [{'a': 1}, {'a': 2}, {'a': 3}]


# 14. Function to create an object from two arrays, one of keys and one of values
def create_object(keys, values):
    obj = {}
    for i in range(len(keys)):
        obj[keys[i]] = values[i]
    return obj

print(create_object(["a", "b"], [1, 2]))  # Output: {'a': 1, 'b': 2}

# 15. Function to get the entries of an object
def get_entries(obj):
    entries = []
    for key, value in obj.items():
        entries.append((key, value))
    return entries

print(get_entries({"a": 1, "b": 2}))  # Output: [('a', 1), ('b', 2)]

# 16. Function to check if an object is empty
def is_object_empty(obj):
    for key in obj:
        return False
    return True

print(is_object_empty({}))  # Output: True


# 17. Function that takes two objects and returns the common keys and their values
def common_keys_values(obj1, obj2):
    common = {}
    for key in obj1:
        if key in obj2 and obj1[key] == obj2[key]:
            common[key] = obj1[key]
    return common

print(common_keys_values({"a": 1, "b": 2}, {"b": 2, "c": 3}))  # Output: {'b': 2}

# 18. Function that finds the keys with the highest value in an object
def keys_with_highest_value(obj):
    max_value = None
    for key in obj:
        if max_value is None or obj[key] > max_value:
            max_value = obj[key]
    highest_keys = []
    for key in obj:
        if obj[key] == max_value:
            highest_keys.append(key)
    return highest_keys

print(keys_with_highest_value({"a": 1, "b": 3, "c": 3}))  # Output: ['b', 'c']


# 19. Function to convert an object to a query string
def object_to_query_string(obj):
    query_string = ""
    for key, value in obj.items():
        query_string += f"{key}={value}&"
    return query_string.rstrip("&")

print(object_to_query_string({"a": 1, "b": 2}))  # Output: 'a=1&b=2'

# 20. Function that returns the nested value of an object given a key path
def get_nested_value(obj, key_path):
    keys = key_path.split(".")
    for key in keys:
        if isinstance(obj, dict) and key in obj:
            obj = obj[key]
        else:
            return None
    return obj

print(get_nested_value({"a": {"b": {"c": 1}}}, "a.b.c"))  # Output: 1