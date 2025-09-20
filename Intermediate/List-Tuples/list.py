list = ["trisha",1,3,5]
print(list)
print(type(list))
print(list[0])
print(list[1:3])
print(list[-3:-1]) #negative indexing it starts from the end of the list with -1

#list methods
list.append("hello") #adds an element to the end of the list
print(list)

#sort method
list1 = [5,3,1,4,2]
list1.sort() #sorts the list in ascending order, It will not directly print the sorted list; we need to print it separately
print(list1)

print(list1.sort()) #it will print None because sort() method does not return any value, but sorting is done in place


#Sorting in descending order
list2 = ["apple","banana","cherry","date"]
list2.sort(reverse=True) 
print(list2)

#reverse method
list2.reverse() #reverses the order of the list
print(list2)

#insert method
list2.insert(1,"blueberry") #inserts an element at a specific index
print(list2)

#remove method
list2.remove("banana") #removes the first occurrence of a specific element
print(list2)
#pop method
list2.pop(2) #removes the element at 2 index (the specified index)
print(list2)
list2.pop() #removes the last element if no index is specified


