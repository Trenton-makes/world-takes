'''
Created on Dec 12, 2018

@author: coditum
'''
def countdown(n):
    print(n)
    if n > 1:
        countdown(n-1)
        
#countdown(4)

def countup(n):
    print(n)
    if n > 1:
        countup(n-1)
    print (n)
    
countup(5)