

pointsPossible = 100
studentName = input("Enter student name: ")

def calcPercentGrade():
    print("calculating grade")
    percent = round(score/pointsPossible,2)


    letterGrade = "ERROR"



    '''
    a= 100-90%
    b= 89-80%
    c= 79-70%
    d= 69-70%
    f= 59-0%
    '''

    if (1.00 >= percent >= .90):
        letterGrade = "A"
    elif(.89 >= percent >= .80):
        letterGrade = "B"
    elif(.79 >= percent >= .70):
        letterGrade = "C"
    elif(.69 >= percent >= .60):
        letterGrade = "D"
    elif(.59 >= percent >= .50):
        letterGrade = "E"
    elif(.59 >= percent >= .50):
        letterGrade = "F"
try:
    score =float(input("Enter test score: "))
    print("score = {}".format(score))
    calcPercentGrade()


except Exception:
    print("you need to enter a valid score")


print("Student = {} \nLetterGrade = {} \nPercentage score = {}".format(studentName,letterGrade,percent))
