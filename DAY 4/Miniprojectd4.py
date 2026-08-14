# Starting data: A list containing tuples of (Name, Marks)
student_records = [
    ("Alice", 85),
    ("Bob", 72),
    ("Charlie", 90),
    ("Alice", 85),  # Notice the duplicate for testing sets later
    ("Diana", 65),
    ("Ethan", 92)
]
print("--- Challenge 1: Student Marks ---")
for name, marks in student_records:
    print(f"Student: {name} | Marks: {marks}")
    print("\n--- Challenge 2: Students scoring above 80 ---")
for name, marks in student_records:
    if marks > 80:
        print(f"{name} scored {marks}")
        print("\n--- Challenge 3: Unique Student Names ---")

# Step A: Extract all names into a set (this removes duplicates automatically)
unique_names_set = {name for name, marks in student_records}

# Step B: Convert the set back into a list if needed
unique_names_list = list(unique_names_set)

print(unique_names_list)