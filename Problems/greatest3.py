#WAP to find the greatest of 3 numbers entered by the user

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))

if(num1 > num2 ):
    print(num1)
elif(num2 > num3):
    print(num2)
else:
    print(num3)

#another  way 
if(num1 >= num2 and num1 >= num3):
    print("first number is greatest : ",num1)
elif(num2 >= num3):
    print("second number is greatest : ", num2)
else:
    print("third number is greatest : ",num3)


#same for 4 number
a = int(input("Enter first no :"))
b = int(input("Enter second no :"))
c = int(input("Enter third no : "))
d = int(input("Enter fourth no : "))

if(a >= b and a >=c and a >= d):
    print("first number is greatest : ",a)
elif(b >= c and b >= d):
    print("second number is greatest : ",b)
elif(c >= d):
    print("third number is greatest : ",c)
else:
    print("fourth number is greatest : ",d)

