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