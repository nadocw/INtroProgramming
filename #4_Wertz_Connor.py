# Homework #4, Wertz, Connor
import showFood
# foodOrder is our list, we can add to it, print it, remove things, whatever we wanna do
foodOrder = []

test = "" #this is a part of the loop

while not test: #basically just means while true
    response = input("How would you like to change your order? (A)dd, (S)how, (R)emove, or e(X)it: ")
    action = response[0] # only look at the first letter of what the user inputs

    if action == "a" or action == "A":
        print("Add to my food order")
        showFood.addSomeFood( foodOrder )
    elif action == "s" or action == "S":
        print("Show orders")
        showFood.showMyFood( foodOrder )
    elif action == "r" or action == "R":
        print("Remove an item")
        showFood.removeFood( foodOrder )
    elif action == "x" or action == "X" or action == "e" or action == "E":
        print("Exit program")
        test = "Done"
    else:
        print("That's not a valid response.")