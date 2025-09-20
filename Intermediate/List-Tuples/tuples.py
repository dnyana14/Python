tuple = (2,3,4)
print(type(tuple))

#we can access tuple elements using indexing and slicing
print(tuple[0])
print(tuple[1:3])  #slicing works the same way as in lists
print(tuple[-3:-1]) #negative indexing

#tuple methods
tup = ("element","problem","solution")
tup.index("problem") #returns the index of the first occurrence of the specified element
print(tup)
print(tup.count("e")) #returns the number of times a specified element appears in the tuple 