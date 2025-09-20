str = "Dnyaneshwari Gaikwad"
for el in str :
    if (el == 'i'):
        print("Next word is started")
        break     #after i will find it will break the loop and stop working
    print(el)
else:             #t means "run this code if the loop wasn’t interrupted by break."
    print("End")

