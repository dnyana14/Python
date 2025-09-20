str = "Dnyaneshwari"
print(str[2 : 5 ])
print(str[1 :]) # It will goes till the end of string if there is not declared a indexing number
print(str[:6])  #It will start from 0 if we not declare indexing number

# In the slicing the character at the end index is not included

#String functions

str1 = "I am enjoying this coding"
print(str.endswith("ing"))           # It will return True if the string ends with the given value otherwise it will return False

print(str1.count("i"))       # It will return the count of the given character in the string means how many times i is present in the sentence

print(str1.find("enjoying"))        # It will return the starting index of the given substring. If it is not found then it will return -1

print(str1.capitalize())             # It will convert the first character of string to uppercase
print(str1)     # It will print original string because string is immutable in python so everytime we have to create a new string if we want to change it

print(str.replace("this", "the"))  # It will replace the given substring with the new substring and return a new string




