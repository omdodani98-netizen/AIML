# Dict stores key value pairs
#creating a dict
student =  {
    "name": "om",
    "age":20,
    "course":"computer science",
    "percentage":85.5
}
# acessing the dict - 
print(student["name"])
#another method : get ()
print(student.get("name"))
# add new data 
student["city"] = "Indore"
print(student)
#update data
student["age"] = 21
print(student)
# delete data
del student["city"]
#or 
student.pop("age")
print(student)
#important dict methods
print(student.keys())
print(student.values())
print(student.items())
# for loop 
marks = [79,88,91]
for mark in marks : print(mark)
# another example
students = ["om " ,  "yogita" , "lovely"]
for student in students : print(student)
for student in students : print(students)
# for loop for dict
students = [
    {"name": "om", "age": 20},
    {"name": "yogita", "age": 21},
    {"name": "lovely", "age": 19}
]

# Loop through each dictionary in the list
for student in students:
    # Loop through keys
    for key in student:
        print(key)
        
    # Loop through values using .values()
    for value in student.values():
        print(value)
       # list of dicts imp
students = [
    {"name": "om", "age": 20},{"name": "yogita", "age": 21},
    {"name": "lovely", "age": 19}]
for student in students:
    print(student["name"], student["age"])
      




