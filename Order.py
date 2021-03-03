# An order is a list of food.
# You can add to, remove from, or show the order
Order = []

# Print foods in Order
def show():
    print("Orders:")
    for food in Order: # for all the things in food
        print(" ~ " + food) #prints out all the items in a list with "~" serving as a bullet point

# Add food to Order
def add():
    newFood = input("What would you like to add to your Order?: ")
    Order.append( newFood )

# Removes a food from Order
def remove():
    foodToRemove = input("What would you like to remove from your Order?: ")
    Order.remove( foodToRemove )