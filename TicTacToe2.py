# Wertz, Connor #5 Tic Tac Toe assignment
# TODO: FIGURE OUT HOW TO ITERATE OVER OBJECTS

import random, sys
import gameFunctions
from time import sleep # This allows for the computer to wait a random amount of time before playing its move

# This is the tic tac toe board
theBoard = { "TL": " ", "TM": " ", "TR": " ",
    "ML": " ", "MM": " ", "MR": " ",
    "BL": " ", "BM": " ", "BR": " " }


# This prints out the board and shows what has been marked
def printBoard( board ):
    print(board["TL"] + "|" + board["TM"] + "|" + board["TR"])
    print("-+-+-")
    print(board["ML"] + "|" + board["MM"] + "|" + board["MR"])
    print("-+-+-")
    print(board["BL"] + "|" + board["BM"] + "|" + board["BR"] + "\n\n")

# Check if there are any winning conditions or all the spaces on the board are full

# Check if space is empty
def emptyCheck( board, play ):
        if board[play] == " ":
            sleep(0.5) # Delays input by half a second to make the game feel more real, instead of instant plays by the computer
            board[play] = "@"
        elif board[play] == "X":
            computerPlay(board) # If filled, the computer will roll again
        elif board[play] == "@":
            computerPlay(board)

def computerPlay( board ): #just a random variable called board to see if it'd work
    move = random.randint(1,9)
    if move == 1:
        play = "TL"
        emptyCheck(board, play)
    elif move == 2:
        play = "TM"
        emptyCheck(board, play)
    elif move == 3:
        play = "TR"
        emptyCheck(board, play)
    elif move == 4:
        play = "ML"
        emptyCheck(board, play)
    elif move == 5:
        play = "MM"
        emptyCheck(board, play)
    elif move == 6:
        play = "MR" 
        emptyCheck(board, play)
    elif move == 7:
        play = "BL" 
        emptyCheck(board, play)
    elif move == 8:
        play = "BM" 
        emptyCheck(board, play)
    elif move == 9:
        play = "BR"         
        emptyCheck(board, play)
    else:
        print("error!")
    
## Main
print("Select a location to play using (TL, TM, TR, ML, MM, MR, BL, BM, BR)")
turn = "X"

# this runs forever
while True:
    printBoard(theBoard)
    gameFunctions.checkGameEnd(theBoard)
    if turn == "A": 
        computerPlay(theBoard)
        turn = "X"
    elif turn == "X":
        move = input("Turn for " + turn + ". Where do you want to play? (USE MY NOTATION PLEASE) ")
        theBoard[move] = turn # fill in the board
        turn = "A"


    # TODO: THIS NEEDS TO BE CHANGED AND CHECK IF THERE ARE VALID NUMBERS ON SCREEN

