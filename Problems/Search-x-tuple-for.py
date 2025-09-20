# tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# x = 16

# for el in tuple :
#     if (el == x) :
#         print("found")

#If I have to print index of specified value then we have to declare it

tup =(2, 4, 6, 8, 6 )
x = 6
idx = 0    

for el in tup:
    if(el == x):
        print("Element found at index", idx) #here we are going to track index element
    idx += 1
