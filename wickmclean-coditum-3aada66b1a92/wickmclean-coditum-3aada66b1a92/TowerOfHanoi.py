'''
Created on Jan 9, 2019

@author: coditum
'''

def tower(number, a, b, c):
    count=1
    if number==0:
        return 0
    #Step 1: Move m-1 disks from source peg to spare peg using function tower()
    count1=tower(number-1, a, c, b)
    
    #Step 2 in recursive algorithm, move disk M from source to target peg
    print("Disk", number, "is moving from peg", a, "to peg", c)
    #step 3 move m-1 disks from spare peg to target peg using function tower()
    count2=tower(number-1, b, a, c)
    return count1+count2+count
    
moves=tower(6, "Source", "Spare", "Target")
print(moves)
