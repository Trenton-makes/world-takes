'''
Created on Dec 21, 2018

@author: wickm
'''
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?

def listuple():
    listos=[]
    n=0
    while len(listos) < 20:
        n+=1
        listos.clear()
        for i in range(1, 21):
            if n%i == 0:
                listos.append(i)
    
    print(n)

print(listuple())