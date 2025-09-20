#Figure out a way to store 9 and 9.0 as separative values in the set.
# Python considers 9 and 9.0 as the same value because they are equal in value and hash to the same value.

#solution 1 : We can store them as strings
set1 = {9, "9.0"}

#solution 2 : We can store them as tuples in dictionary
set2 = {(9, "int"),
         (9.0, "float")}
print(set2)
print(set1)