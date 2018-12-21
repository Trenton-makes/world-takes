'''
Created on Nov 18, 2018

@author: wickm
'''
'''
Created on Nov 16, 2018

@author: coditum
'''



def printboard(list4):
    for row in list4:
        print("|"+row[0]+"|"+ row[1]+"|"+row[2]+"|")
        print("-------")

def usermove(piece, list4):
    move=input("Enter the coordinates of your move")
    move=move.split(",")
    row=move[0]
    row=int(row)
    column=move[1]
    column=int(column)
    list4[row][column]=piece
    
def checkwin(piece, list4):
    for r in range (3):
        if list4[r][0]==piece and list4[r][1]==piece and list4[r][2]==piece:
            print("you won!")
            exit()
        if list4[0][r]==piece and list4[1][r]==piece and list4[2][r]==piece:
            print('You won!')
            exit()
    if list4[0][0]==piece and list4[1][1]==piece and list4[2][2]==piece:
            print('you won!')
            exit()
    if list4[2][0]==piece and list4[1][1]==piece and list4[0][2]==piece:
            print('you won!')
            exit()


    
  
def play():
    list1=[" ", " ", " "]
    list2=[" ", " ", " "]
    list3=[" ", " ", " "]
    list4=[list1, list2, list3]
    printboard(list4)
    for turn in range (9):
        if turn %2 == 0:
            piece='x'
        else:
            piece='o'
        usermove(piece, list4)
        printboard(list4)
        checkwin(piece, list4)
        
play()