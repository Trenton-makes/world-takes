'''
Created on Nov 19, 2018

@author: coditum
'''
ROW_VARIABLE = 7
nextrows=[5, 5, 5, 5, 5, 5, 5]

def printboard():
    count=0
    while count < 6:
        print("".join(board[count]))
        count += 1

def makeboard():
    board=[]
    for row2 in range(6):
        row=["[ ]"]*7
        board.append(row)
    return(board)

def userturn(piece):
    while True:
        usercolumn = int(input('Type in a column, 0 to 6'))
        if usercolumn <0 or usercolumn > 6:
            continue
        userrow = nextrows[usercolumn]
        if userrow < 0:
            continue
        nextrows[usercolumn] = userrow - 1
        board[userrow][usercolumn]=piece
        return

def winning(piece):
    for r in range(6):
        for c in range(4):
            if board[r][c] == piece and board[r][c+1] == piece \
             and board[r][c+2] == piece and board[r][c+3]==piece:
                return True
def play():
    printboard()
    for turn in range (42):
        if turn %2 == 0:
            piece='[x]'
        else:
            piece='[o]'
        userturn(piece)
        printboard()
        if winning(piece) == True:
            print('congrats!')
            return
        
board=makeboard()
play()