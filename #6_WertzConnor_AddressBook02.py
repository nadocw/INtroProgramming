# Assignment #6, Connor Wertz

print("What's up, I'm here so that you can list out your fav contacts.")

fileName = input("What is your file named: ")
myContacts = fileName + ".txt"
open(myContacts, "a+", encoding="utf-8")

done = ""
while not done:
    done = input("Do you want to (R)ead your address or (A)dd new contacts? You can also (Q)uit: ")
    answer = done[0]

    if answer in [ "r", "R" ]:
        print("I'm reading")
        # opening file to read it
        handle = open(myContacts, "r")
        # line = input(int("Which line do you want to read: "))
        facts = handle.read()
        print(facts)
        handle.close() # you have to close file or it won't work
        done = ""


    elif answer in [ "a", "A" ]:
        print("I'm writing")
        # add to my file
        handle = open(myContacts,"a+", encoding="utf-8")  # The "a+" here stands for append, append add things to the file, if you open in write mode it'll erase everything
        myFriend = []
        for i in range (1):
            myFriend.append(input("What's this person's name: "))
            myFriend.append(input("What's this person's birthday: "))
            myFriend.append(input("What's this person's favorite food: "))
            myFriend.append(input("What is this person's political affiliation: "))
            myFriend.append(input("How attractive is this person: "))
        print(myFriend)
        handle.write(str(myFriend) + "\n")
        handle.close()
        done = ""

    elif answer in ["q", "Q", "D", "d"]:
        done = "Finished"
        print("Goodbye!")

    else:
        print("Bro really? Just type what I told you to type")
        done = ""