#WAP to check a list contains a palindrome of elements (Hint : Use the copy() method of list)
# Palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward, such as madam or racecar. 
# ex : madam, 121, mam, racecar 

list = [1,2,3,2,1]

copy_list = list.copy() #create a copy of the original list
copy_list.reverse() #reverse the copied list

if(list == copy_list):
    print("The list contains a palindrome")
else:
    print("The list does not contain a palindrome")