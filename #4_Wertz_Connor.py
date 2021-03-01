# Homework #4, Wertz, Connor

# Order is our list, we can add to it, print it, remove things, whatever we wanna do
import Order

while True:
    userInput = input("How would you like to change your order? (A)dd, (S)how, (R)emove, or e(X)it: ")
    action = userInput[0]

    if action == "a" or action == "A":
        Order.add()
    elif action == "s" or action == "S":
        Order.show()
    elif action == "r" or action == "R":
        Order.remove()
    elif action == "x" or action == "X" or action == "e" or action == "E":
        print("Exit program")
        exit()
    else:
        print("That's not a valid response.")