print("exam grade calculator")

nameOfExam = input("What is the name of exam?")
if nameOfExam.lower() == "computer science":  
    print("computer science")
else:
    print("this one is not your subject, sorry buddy!")
    
maxPossibleScore = int(input("What is the maximum possible score?"))
score = int(input("enter you code:"))

if score >= 100:
    print("maximum score!")
elif score >= 90: 
    print("your final score is A+")
elif score >= 80:
    print("Your final score is A-")
elif score >= 70:
    print("Your final score is B")
elif score >= 60:
    print("Your final score is C")
elif score >= 50:
    print("Your final score is D")
elif score >= 40:
    print("Your final score is U")
else:
    print("You lost the exam buddy, you need to repeit it!")