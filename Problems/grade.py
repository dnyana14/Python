#Grade students based on their score
# marks >= 90, grade ='A'
# 90 > mark >= 80, grade = 'B'
# 80 > mark >= 70, grade = 'C'
# 70 > mark, grade = 'D'

marks = 85   # we can give input here using input() function
if(marks >= 90):
    grade = 'A'
elif(marks >= 80 and marks < 90):
    grade = 'B'
elif(marks >= 70 and marks < 80):
    grade = 'C'
else:
    grade = 'D'

print("Your grade is: " + grade)