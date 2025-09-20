#Print odd number throught loop from 1 to 10

i = 0

while i < 10 :
    if(i%2 == 0):  #if the i has remainder 0 after divided by 2, then condition says add 1 on that i
        i += 1       
        continue    # after adding one continue the loop after the continue statement, It is skipping the even number
    print(i)
    i += 1