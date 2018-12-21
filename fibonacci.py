'''
Created on Dec 14, 2018

@author: wickm
'''
#Return the value for the i-th number in the fibonacci sequence

def fibonacci(i):
    if i == 1:
        return 1
    if i==2:
        return 1
    fib=fibonacci(i-1)+fibonacci(i-2)
    return fib
x=fibonacci(10)
print(x)