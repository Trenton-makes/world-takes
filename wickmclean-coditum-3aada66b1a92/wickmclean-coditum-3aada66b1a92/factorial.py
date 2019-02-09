'''
Created on Dec 12, 2018

@author: coditum
'''
def factorial(n):
    if n ==1:
        return 1
    else:
        return n*factorial(n-1)

answer=factorial(2)
print(answer)