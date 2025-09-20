info = {
    "name": "Dictionary",
    "description": "Learn how to use dictionaries in Python.",
    "difficulty": "Intermediate",
}
print(info)

dict = {
    "name" : "Dnyana",
    "age" : 21,
    "is_student" : "Flase",
    "courses" : [ "Python","JS"],  #list 
    "Skill" : ("HTML","CSS"), #tuple
    "marks" : 8.23,
}

# we cant use mutable data types like list and dictionary as keys in dictionarys 
# we can use immutable data types like string, numbers and tuples as keys in dictionarys

print(dict["age"]) # accessing value using key
print(dict.get("name")) # accessing value using get method

#We can change the value of a key in dictionary
dict["age"] = 22
dict["Surname"] = "Gaikwad" # adding new key-value pair
print(dict)


#null dictionary
empty_dict = {}
empty_dict["Name"] = "Dnyaneshwari"
print(empty_dict)

