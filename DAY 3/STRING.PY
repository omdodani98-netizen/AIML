#sring 
name = "yogita"
print(name)
#indexing in string (positive)
print(name[1])
print(name[2])
print(name[3])
# (negative indexing)
print(name[-1])
print(name[-5])
#string slicing 
print(name[1:5])
print(name[0:3])
# advanced 
print(name[::2])
print(name[::-1])
#using len() length
print(len(name))
#string methods
print(name.upper)
print(name.lower)
print(name.strip)
print(name.replace("yogita", "om"))
# sentances 
sentance = "i like python"
word = sentance.split()
print(word)
print(sentance.find("like"))
print(name.startswith("yo"))
print(name.endswith("ta"))
#f string
print(f"my name is {name} and my sentance is {sentance}")




