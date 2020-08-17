import tkinter as tk
import sys
import os

HEIGHT = 600
WIDTH = 600
PADDING = 0.02
BUTTONWIDTH = 0.32
root = tk.Tk()
root.title("Tic Tac Toe")
x = tk.PhotoImage(file = "x.gif")
o = tk.PhotoImage(file = "o.gif")
winner = ""
turn = "X"
TK_SILENCE_DEPRECATION=1
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='black')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

b1 = tk.Button(frame, bg='gray', command = lambda: click(b1))
b1.place(relx=0, rely=0, relwidth=BUTTONWIDTH, relheight=BUTTONWIDTH)

b2 = tk.Button(frame, bg='gray', command = lambda: click(b2))
b2.place(relx=0.34, rely=0, relwidth=BUTTONWIDTH, relheight=BUTTONWIDTH)

b3 = tk.Button(frame, bg='gray', command = lambda: click(b3))
b3.place(relx=0.68, rely=0, relwidth=BUTTONWIDTH, relheight=BUTTONWIDTH)

b4 = tk.Button(frame, bg='gray', command = lambda: click(b4))
b4.place(relx=0, rely=0.34, relwidth=BUTTONWIDTH, relheight=BUTTONWIDTH)

b5 = tk.Button(frame, bg='gray', command = lambda: click(b5))
b5.place(relx=0.34, rely=0.34, relwidth=BUTTONWIDTH, relheight=BUTTONWIDTH)

b6 = tk.Button(frame, bg='gray', command = lambda: click(b6))
b6.place(relx=0.68, rely=0.34, relwidth=BUTTONWIDTH, relheight=BUTTONWIDTH)

b7 = tk.Button(frame, bg='gray', command = lambda: click(b7))
b7.place(relx=0, rely=0.68, relwidth=BUTTONWIDTH, relheight=BUTTONWIDTH)

b8 = tk.Button(frame, bg='gray', command = lambda: click(b8))
b8.place(relx=0.34, rely=0.68, relwidth=BUTTONWIDTH, relheight=BUTTONWIDTH)

b9 = tk.Button(frame, bg='gray', command = lambda: click(b9))
b9.place(relx=0.68, rely=0.68, relwidth=BUTTONWIDTH, relheight=BUTTONWIDTH)

def click(button):
    global turn, winner
    if turn == "X":
        button.config(image = x, state = "disabled")
        turn = "O"
    elif turn == "O":
        button.config(image = o, state = "disabled")
        turn = "X"
    if checkForWin():
        changeWinnerName()
        label = tk.Label(frame, text="Winner is " + winner, font=100)
        label.place(relx=0, rely=0, relwidth=1, relheight=1)
    elif checkForTie():
        label = tk.Label(frame, text="It's a tie", font=100)
        label.place(relx=0, rely=0, relwidth=1, relheight=1)

def checkForTie():
    if (b1.cget('state') == b2.cget('state') == b3.cget('state')
    == b4.cget('state') == b5.cget('state') == b6.cget('state')
    == b7.cget('state') == b8.cget('state') == b9.cget('state') == "disabled"):
        return True
    else:
        return False

def changeWinnerName():
    global winner
    if winner == "pyimage1":
        winner = "X"
    elif winner == "pyimage2":
        winner = "O"

def checkRows(): 
    global winner
    row1 = b1.cget('image') == b2.cget('image') == b3.cget('image') != ""
    row2 = b4.cget('image') == b5.cget('image') == b6.cget('image') != ""
    row3 = b7.cget('image') == b8.cget('image') == b9.cget('image') != ""
    if row1:
        winner = b1.cget('image')
    elif row2:
        winner = b4.cget('image')
    elif row3:
        winner = b7.cget('image')
    if row1 or row2 or row3:
        return True
    else:
        return False

def checkCols():
    global winner
    col1 = b1.cget('image') == b4.cget('image') == b7.cget('image') != ""
    col2 = b2.cget('image') == b5.cget('image') == b8.cget('image') != ""
    col3 = b3.cget('image') == b6.cget('image') == b9.cget('image') != ""
    if col1:
        winner = b1.cget('image')
    elif col2:
        winner = b2.cget('image')
    elif col3:
        winner = b3.cget('image')

    if col1 or col2 or col3:
        return True
    else:
        return False

def checkDiags():
    global winner
    diag1 = b1.cget('image') == b5.cget('image') == b9.cget('image') != ""
    diag2 = b3.cget('image') == b5.cget('image') == b7.cget('image') != ""
    if diag1:
        winner = b1.cget('image')
    elif diag2:
        winner = b3.cget('image')

    if diag1 or diag2:
        return True
    else:
        return False

def checkForWin():
    if checkRows() or checkCols() or checkDiags():
        return True

root.mainloop()