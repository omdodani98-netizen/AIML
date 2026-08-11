#marks calculator 
english = int(input("ENGLISH MARKS = "))
hindi = int(input("HINDI MARKS = "))
chemistry = int(input("CHEMISTRY MARKS = "))
physics = int(input("PHYSICS MARKS = "))
biology = int(input("BIOLOGY MARKS = "))
 # calculation 
Total = ( english + hindi + chemistry + physics + biology )
print("Total marks = " , Total , "/500")
percentage = Total/5
print("percentages are  = " , percentage ,"%")