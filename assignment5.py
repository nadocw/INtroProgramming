# take the code from the book, have the user play and then make the computer play

import random

# This is the tic tac toe board
theBoard = { "TL" : " ", "TM" : " ", "TR" : " ", "ML" : " ", "MM" : " ", "MR" : " ", "BL" : " ", "BM" : " ", "BR" : " " }

# This prints out the board and shows what has been marked
def printBoard( board ):
    print(board["TL"] + "|" + board["TM"] + "|" + board["TR"])
    print("-+-+-")
    print(board["ML"] + "|" + board["MM"] + "|" + board["MR"])
    print("-+-+-")
    print(board["BL"] + "|" + board["BM"] + "|" + board["BR"])

def computerPlay( amelia ): #just a random variable called amelia to see if it'd work
    done = ""
    while not done:
        move = random.randint(1,9)
        if move == 1:
            play = "TL"
            if amelia [play] == " ":
                amelia[play] = "@"
                done = True
        elif move == 2:
            play = "TM"
            if amelia [play] == " ":
                amelia[play] = "@"
                done = True
        elif move == 3:
            if amelia [play] == " ":
                amelia[play] = "@"
                done = True
            play = "TR"
        else:
            print("error!")
    print(play)

printBoard(theBoard)
print("You get to be X! Select a location to play using (TL, MM, BR)")
turn = "X"
for i in range(9):
    printBoard(theBoard)
    move = input("Turn for " + turn + ". Where do you want to play? (USE MY NOTATION PLEASE) ")
    theBoard[move] = turn # I'm getting confused here
    if turn == "A": #THIS NEEDS TO BE CHANGED AND CHECK IF THERE ARE VALID NUMBERS ON SCREEN
        # Put a subroutine (functuion) that can pick as the computer, function here that looks at the board
        # and randomizes 9 numbers
        computerPlay( theBoard )
        turn = "J"
    else: turn = "A"

printBoard(theBoard)