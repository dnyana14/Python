dict = {
    "Name": "KeysMethods",
    "Description": "Methods and properties of the Keys object in Python."
}

dict.keys()    #return all the keys in the dictionary
dict.get("Name")  #return the value of the specified key  

print(dict["Description"])  #return the value of the specified key
print(dict.get("Name"))  #return the value of the specified key    

print(dict.get("Age"))  #return None if the key does not exist
#print(dict["Age"])  #raise an error if the key does not exist

print(dict.update({"Age": 30}))  #update the value of the specified key
print(dict)  #print the updated dictionary
