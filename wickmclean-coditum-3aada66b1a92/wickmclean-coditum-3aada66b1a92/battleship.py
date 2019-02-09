'''
Created on Dec 19, 2018

@author: coditum
'''

from random import randint
def makeboard():
    board=[]
    for i in range(5):
        row=["[ ]"]*5
        board.append(row)
    return(board)

def printboard(board):
    print("   1  2  3  4  5 ")
    print('A', "".join(board[0]))
    print("B", "".join(board[1]))
    print("C", "".join(board[2]))
    print("D", "".join(board[3]))
    print("E", "".join(board[4]))
    
def placeships():
    battleboard=makeboard()
    printboard(battleboard)
    for i in range(5):
        shipplace=input("Where do you want your ship to go?")
        row=getrow(shipplace[0])
        col=int(shipplace[1])-1
        battleboard[row][col]="[x]"
        printboard(battleboard)
    return battleboard

def getrow(row):
    if row == "a":
        return 0
    if row == "b":
        return 1
    if row =="c":
        return 2
    if row =="d":
        return 3
    if row =="e":
        return 4
    return 5
def computerships():
    battleboard=makeboard()
    i=0
    while i < 5:
        row=randint (0, 4)
        col=randint (0, 4)
        if battleboard[row][col] != "[x]":
            battleboard[row][col]="[x]"
            i+=1
    return battleboard

def userturn(guesses, userhits, computerboard):
    while True:
        printboard(guesses)
        coords=input("What are the coordinates of your guess?")
        row=getrow(coords[0])
        col=int(coords[1])-1
        if row ==5 or col<0 or col > 4:
            if row == 5:
                print("Please enter a row between A and E")
            if col <0 or col >4:
                print("Please enter a column between 1 and 5")
            continue
        if guesses[row][col]!="[ ]":
            print("You already went there try again!")
            continue
        if computerboard[row][col]=="[x]":
            userhits.append(coords)
            guesses[row][col]="[x]"
            print("Congrats you hit!")
        else:
            guesses[row][col]="[o]"
            print("You missed")
        break

def computerturn(computerguesses):
    while True:
        row=randint(0,4)
        col=randint(0,4)
        
        if computerguesses[row][col]!="[ ]":
            continue 
        if battleboard[row][col]=="[x]":
            computerhits.append(7)
            computerguesses[row][col]="[x]"
            print("The computer got a hit!")
        else:
            computerguesses[row][col]="[o]"
            print("The computer missed!")
        break



computerguesses=makeboard()
guesses=makeboard()    
userhits=[]
computerhits=[]
computerboard=computerships()
battleboard=placeships()

while len(userhits)<5 and len(computerhits)<5:
    userturn(guesses, userhits, computerboard) 
    computerturn(computerguesses)
if len(userhits) > len(computerhits):
    print("congratulations you won!")
else:
    print("Sorry, the computer won!")    