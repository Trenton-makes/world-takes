'''
Created on Nov 9, 2018

@author: coditum
'''
square=4
for y in range (square):
    for x in range (square-y-1):
        print(' ', end="")
    for x in range(y+1):
        print('* ', end="")
    print()

diamond=3
for y in range(diamond, -1, -1):
    for x in range (diamond-y+1):
        print(' ', end="")
    for x in range(y):
        print('* ', end="")
    print()