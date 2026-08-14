# ==========================================
# Exercise 1: List Practice
# ==========================================

subjects = [
    "Physics",
    "Chemistry",
    "Mathematics",
    "Computer Science",
    "English"
]

# Print first subject (index 0)
print(f"First subject   : {subjects[0]}")

# Print last subject (index -1)
print(f"Last subject    : {subjects[-1]}")

# Print number of subjects using len()
print(f"Number of subjects: {len(subjects)}")
# ==========================================
# Exercise 2: List Practice - Calculations
# ==========================================

marks = [78, 82, 91, 88, 75]

# Calculate total, average, highest, and lowest
total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

# Print results
print(f"Total   : {total}")
print(f"Average : {average}")
print(f"Highest : {highest}")
print(f"Lowest  : {lowest}")