print("FAKE FAN FINDER")

fakeFan = input('what is your favorite "anime"?')
fakeFan = fakeFan.lower()
fakeFan = fakeFan.replace(" ","")
if fakeFan == "naruto" :
    print("oh really!!!")
    faveCharacter = input("name of any of the characters?")
    if faveCharacter == "itachi":
        print("no way, it's my favorite one too!!")
    else:
        print("very intereseting")
elif fakeFan == "onepiece":
    print("very interesting anime")
else:
    print("Aww, sad times")