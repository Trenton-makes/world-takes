'''
Created on Dec 14, 2018

@author: wickm
'''
def factorial(n):
    if n ==1:
        fact=n
        return fact
    else:
        fact=n*factorial(n-1)
        return fact

answer=factorial(4)
print(answer)