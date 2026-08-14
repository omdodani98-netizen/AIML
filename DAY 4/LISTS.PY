# LISTS IN PYTHON 
students = ["RAHUL" , "AMAN" , "PRIYA"]
print(students)
marks = ["20" , "40" , "50"]
data = ["om" , "90"]
print(students , marks , data )
#indexing in lists
print(students[0])
print(data[1])
print(marks[-3])
# lists slicing
print(students[0:2])
print(marks[1:2])
# chaning lists values 
data = ["20" , "40" , "60"]
print(data)
data[1] = 100
print(data)
# lists methods 
# 1. Append()
students = ["om" , "lovely" , "yogita", "hehe"]
students.append("nishchay")
print(students)
# 2. insert()
students.insert(1 , " dovely ")
print(students)
# 3. remove()
students.remove("hehe")
print(students)
# 4. pop()
students.pop(1)
print(students)
# 5. sort()
numbers = ["20" , "30" , "10" , "80" , "50"]
numbers.sort()
print(numbers)
# 6. reverse sort
numbers.sort(reverse=True)
print(numbers)
# 7. usefull built-in functions
print(len(numbers))
print(max(numbers))
print(min(numbers))

