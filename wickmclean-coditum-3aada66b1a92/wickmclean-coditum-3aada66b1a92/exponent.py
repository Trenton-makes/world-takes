'''
Created on Jan 9, 2019

@author: coditum
'''

def expfun(x,y):
    if y==1:
        return x
    result=x*expfun(x,y-1)
    return result

x=expfun(4,6)
print(x)