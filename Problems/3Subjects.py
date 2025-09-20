#WAP to enter marks of three subjects from the user and store them in a dictionary. Start with an empty dictionary and add one by one. Use subject name as key and mark as value

dict = {}

x = int(input("Enter marks of Subject 1: "))
dict.update({"Subject 1": x})
y = int(input("Enter marks of Subject 2: "))
dict.update({"Subject 2": y})
z = int(input("Enter marks of Subject 3: "))
dict.update({"Subject 3": z})
print(dict)
