print("generation identifier")
yearOfBirth = int(input("which year were you born?"))

if yearOfBirth  >= 1883 and yearOfBirth  <= 1900: 
    print("You are part of the lost generation")
elif yearOfBirth >= 1901 and yearOfBirth <= 1927:
    print("You are part of the greatest generation")
elif yearOfBirth>= 1928 and yearOfBirth <= 1945:
    print("You are part of the silent generation")
elif yearOfBirth >= 1946 and yearOfBirth <= 1964:
    print("You are part of the baby boomers generation")
elif yearOfBirth >= 1965 and yearOfBirth <= 1980:
    print("You are part of the x generation")
elif yearOfBirth >= 1981 and yearOfBirth <= 1996:
    print("You are part of the millenials generation")
elif yearOfBirth >= 1997 and yearOfBirth <= 2012:
    print("You are part og the z generation")
elif yearOfBirth >= 2012 and yearOfBirth <= 2024:
    print("You are part of the alpha generation")
else:
    print("If you aren't in this list, you don't exist")
    
    

    