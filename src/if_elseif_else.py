
age = 6

even = (age % 2 == 0) # boolean: is the age even
fiveToSeven = (7 >= age >= 5) #boolean: is the age between 5 & 7

if (even or fiveToSeven): #even is true OR fiveToSeven is true
    print("or")

if (even and fiveToSeven): #even is true AND fiveToSeven is true
    print("and")
