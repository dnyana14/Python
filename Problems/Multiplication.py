#print the multiplication table of a n number

number = int(input("Enter a number: "))

# first user will take the input, then we have to apply the logic that whatever user enter a number , we have to print the multiplication table of that number. for that I have to create a loop and in that loop there will be a variable which will be multiplied with 1 to 10, 

count = 1
while count <=10 :
    result = number * count       # whatever number user enter it will be multiplied with count variable
    count += 1

    print("the multiplication table is here", result)