def checkGameEnd(board):    
    if board["TL"] != " " and board["TM"] != " " and board["TR"] != " " and board["ML"] != " " and board["MM"] != " " and board["MR"] != " " and board["BL"] != " " and board["BM"] != " " and board["BR"] != " ":      
        print("Nobody wins! Exiting game.")
        exit()
    elif board["TL"] == "X" and board["TM"] == "X" and board["TR"] == "X" or board["ML"] == "X" and  board["MM"] == "X" and board["MR"] == "X" or board["BL"] == "X" and board["BM"] == "X" and board["BR"] == "X" or board["TL"] == "X" and board["ML"] == "X" and board["BL"] == "X" or board["TM"] == "X" and board["MM"] == "X" and board["BM"] == "X" or board["TR"] == "X" and board["MR"] == "X" and board["BR"] == "X" or board["TR"] == "X" and board["MM"] == "X" and board["BL"] == "X" or board["TL"] == "X" and board["MM"] == "X" and board["BR"] == "X":
        print("You win! Exiting game.") 
        exit()
    elif board["TL"] == "@" and board["TM"] == "@" and board["TR"] == "@" or board["ML"] == "@" and  board["MM"] == "@" and board["MR"] == "@" or board["BL"] == "@" and board["BM"] == "@" and board["BR"] == "@" or board["TL"] == "@" and board["ML"] == "@" and board["BL"] == "@" or board["TM"] == "@" and board["MM"] == "@" and board["BM"] == "@" or board["TR"] == "@" and board["MR"] == "@" and board["BR"] == "@" or board["TR"] == "@" and board["MM"] == "@" and board["BL"] == "@" or board["TL"] == "@" and board["MM"] == "@" and board["BR"] == "@":
        print("Too bad, the computer wins! Exiting game.") 
        exit()

