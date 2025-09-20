# We can insert a dictionary inside another dictionary
# This is called nested dictionary 
dict = {
    "name": "Dnyana",
    "Marks": {
        "Math": 90,
        "Science": 85,
        "English": 88
    },
    "CGPA" : 8.23
}
print(dict)
print(dict["Marks"]["Math"]) # accessing value of nested dictionary
#we can also insert list in dictionary