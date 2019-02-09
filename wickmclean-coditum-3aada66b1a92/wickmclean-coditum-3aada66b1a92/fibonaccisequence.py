'''
Created on Dec 14, 2018

@author: coditum
'''
def fibonacci(i):
    if i == 1:
        return 1
    if i==2:
        return 1
    fib=fibonacci(i-1)+fibonacci(i-2)
    return fib
x=fibonacci(2)
print(x)