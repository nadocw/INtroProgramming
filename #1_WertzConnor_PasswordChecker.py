# #1 Wertz, Connor EXTRA CREDIT Programming Assignment #1 -- Passwords and File I/O

# Ask user name of .txt file in default directory
fileName = input("What is your .txt named? Do not type file extension: ")
# Add .txt to end of user filename input
theFile = fileName + ".txt"

thatfile = open(theFile,"r")

# Looks at first line of .txt file, removes the paragraph break from end
password = (thatfile.readline())
shortPass = password[:-1]

# Get password from user
userPassword = input("What's the password?: ")

# Check if the user input is the same as the first line of .txt minus the paragraph break

if userPassword == shortPass:
    print("You got it right!")
    print(thatfile.read())
else:
    print("Incorrect Password!")


thatfile.close