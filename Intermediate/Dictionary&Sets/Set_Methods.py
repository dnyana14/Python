#Methods Of Set

Set = {1,2,3,4,5}

#add() method

Set.add(6)  #adds an element to the set
Set.add(2) #if the element is already present, it will not add it again
print(Set)

#remove() method
Set.remove(3)  #removes an element from the set, raises KeyError if the element is not found
print(Set)


#Clear() method
Set.clear()  #removes all elements from the set
print(Set)

#Pop() method
Set = {1,2,3,4,5}
Set.pop()  #removes and returns an arbitrary element from the set, raises KeyError if the set is empty

print(Set)



#Union() method
set1 = {1,2,3}
set2 = {4,5,6}
set3 = set1.union(set2)  #returns a new set that is the union of two sets
print(set3)

#Intersection() method
set4 = {1,2,3,4}
set5 = {3,4,5,6}    
set6 = set4.intersection(set5)  #returns a new set that is the intersection of two sets
print(set6)

#Update() method
set4.update(set5)  #updates the set with the union of itself and another
print(set4)