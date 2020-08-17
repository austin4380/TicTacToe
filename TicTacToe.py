l = [" ", " ", " ", 
     " ", " ", " ", 
     " ", " ", " "]
winner = ""
player = "X"

def turn(player):
    x = input(player + "'s Turn. Choose a position 1-9: ")

    while x not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] or l[int(x) - 1] != " ":
        x = input("Invalid position. Choose a number corresponding to an area of the game board: ")

    for i in range(1, 10):
        if x == str(i):
            l[i-1] = player

def checkRows(): 
    global winner
    row1 = l[0] == l[1] == l[2] != " "
    row2 = l[3] == l[4] == l[5] != " "
    row3 = l[6] == l[7] == l[8] != " "
    if row1:
        winner = l[0]
    elif row2:
        winner = l[3]
    elif row3:
        winner = l[6]
    if row1 or row2 or row3:
        return True
    else:
        return False

def checkCols():
    global winner
    col1 = l[0] == l[3] == l[6] != " "
    col2 = l[1] == l[4] == l[7] != " "
    col3 = l[2] == l[5] == l[8] != " "
    if col1:
        winner = l[0]
    elif col2:
        winner = l[1]
    elif col3:
        winner = l[2]

    if col1 or col2 or col3:
        return True
    else:
        return False

def checkDiags():
    global winner
    diag1 = l[0] == l[4] == l[8] != " "
    diag2 = l[2] == l[4] == l[6] != " "
    if diag1:
        winner = l[0]
    elif diag2:
        winner = l[2]

    if diag1 or diag2:
        return True
    else:
        return False

def flipPlayer():
    global player
    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"

def checkForWin():
    if checkRows() or checkCols() or checkDiags():
        return True

def printBoard():
    print (" " + l[0] + " | " + l[1] + " | " + l[2] + " ")
    print ("-----------")
    print (" " + l[3] + " | " + l[4] + " | " + l[5] + " ")
    print ("-----------")
    print (" " + l[6] + " | " + l[7] + " | " + l[8] + " ")

while (checkForWin() != True):
    printBoard()
    turn(player)
    checkForWin()
    flipPlayer()
printBoard()
flipPlayer()
print ("Congratulations " + player + "!!!")