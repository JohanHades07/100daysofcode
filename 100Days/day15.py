print("Infantil game")

infantilGame = input("What animal do you want?")
infantilGame = infantilGame.lower()
infantilGame = infantilGame.replace("","")
if infantilGame == "cow":
        print("A cow goes moo!!!")
        faveCharacter = input("if the animal goes ouuuu!!!")
        if faveCharacter == "ouuuu":
            print("a wolf goes ouuuu!!")
        else: 
            print("I can't hear that noise!")
elif infantilGame == "guau guau":
    print("It is a dog!!!")
else:
    print("no wait, it is a cat!")
exit = ""
while exit != "yes":
    print(" ")
    exit = input("Exit?:")
