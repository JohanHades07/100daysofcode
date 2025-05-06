print("seconds in a year")

SecondsInAMinute = 60
print(SecondsInAMinute)
SecondsInAnHour = SecondsInAMinute * 60
print(SecondsInAnHour)
secondsInADay = SecondsInAnHour * 24
print(secondsInADay)
secondsInAYear = 365 * secondsInADay
print(secondsInAYear)
secondsInALeap = 366 * secondsInADay
print(secondsInALeap)

if secondsInAYear == 31536000:
    print("normal year")
elif secondsInALeap == 31622400:
    print("leap year!!")
else:
    print("incorrect value")




