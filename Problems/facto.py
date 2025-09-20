#WAP to find facorial of n  numbers (using for)
n = 3

fact = 1    

for i in range(1, n+1):  #here 1 should be write because index is started from 0
    fact *= i
   
print("factorial :", fact)
