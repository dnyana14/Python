#Dictionary Methods

dict = {
    "name":"Dnyaneshwari",
    "Marks":{
        "Math":90,  
        "Science":85,
        "English":88
    },
    "CGPA":8.23
}

print(dict)
print(dict["Marks"]["Math"]) # accessing value of nested dictionary

#accessing the keys of dictionary
print(dict.keys()) # returns a list of all keys in the dictionary, not return nested keys
print(list(dict.keys())) # converting keys to list

#accessing the values of dictionary
print(dict.values())

print(dict.items())
