print("tip calculator")

ourBill = float(input("How much did you spend?"))
porcantageOfTheTip = int(input("How porcentage do you want to tip?"))
peopleInMyGroup = int(input("how many people in your group?"))
answer = ourBill / peopleInMyGroup + porcantageOfTheTip / peopleInMyGroup
answer = round(answer,2)
print("you each owe", answer)

# respuesta de chat gpt
print("Tip Calculator")

ourBill = float(input("How much did you spend? "))
percentageOfTheTip = int(input("What percentage do you want to tip? "))
peopleInMyGroup = int(input("How many people in your group? "))
totalTip = ourBill * (percentageOfTheTip / 100)
totalAmount = ourBill + totalTip
answer = totalAmount / peopleInMyGroup
answer = round(answer, 2)
print("You each owe", answer)



