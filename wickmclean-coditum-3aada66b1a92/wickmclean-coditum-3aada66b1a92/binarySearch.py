'''
Created on Jan 9, 2019

@author: coditum
'''
array=[10,20,30,40,50,60,70,80,90,100]

def binarysearch(array,x):
    larray=len(array)
    midpoint=int(larray/2)
    findnum=array[midpoint]
    if findnum==x:
        return midpoint
    elif x<findnum:
        return binarysearch(array[:midpoint], x)
    elif x>findnum:
        return binarysearch(array[midpoint:], x)+midpoint
    
x=binarysearch(array, 91)
print(x)