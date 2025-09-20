#Search for number x in this tuple using loop
#[1,4,9,16,25,36,49,64,81,100]

#first print the elements of the tuple

# tuple = (1,4,9,16,25,36,49,64,81,100)

# count = 0
# while count < len(tuple) :
#     print(tuple[count])
#     count += 1

    #now search for a number x in this tuple
tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 36
i = 0 #index variable
while  i < len(tuple) :
    if tuple[i] == x :
          print("Found at index", i)
    i += 1

#the loop is going on till the codition is there