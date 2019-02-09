'''
Created on Nov 9, 2018

@author: coditum
'''
square=4
for y in range (square):
    for x in range (square-y-1):
        print(' ', end="")
    for x in range(y+1):
        print('x ', end="")
    print()
        
    