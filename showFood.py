# These three functions are what the user calls when they wanna add, remove, or show all the items on the list

def showMyFood( food ):
    for items in food: # for all the things in food
        print(" ~ " + items) #prints out all the items in a list with "~" serving as a bullet point
    return food # is it necessary to have this?


# Adds a function that lets me add items to foodOrder
def addSomeFood( food ):
    newFood = input("What would you like to add to your order? ")
    food.append( newFood )
    return food

# Adds a function that removes an item from foodOrder
def removeFood( food ):
    deleteThis = input("What would you like to remove from your order?")
    food.remove( deleteThis )
    return food