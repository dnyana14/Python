#print the elements of the following list using while loop
#[1,4,9,16,25,36,49,64,81,100]

# firstly, there will looping from 1 to 10, and then we have to multiply this with itself 

count = 1
while count <= 10 :
    result = count * count
    count += 1
    print(result)

# print ["Ironman", "Captain America", "Black Panther", "Hulk", "Thor", "Doctor Strange"] through while loop

heroes = ["Ironman", "Captain America", "Black Panther", "Hulk", "Thor", "Doctor Strange"]
count = 0
while count < len(heroes) :
    print(heroes[count])
    count += 1
#len function will give the length of the list, and in while loop we have to use < operator because index starts from 0