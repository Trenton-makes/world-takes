'''
Created on Dec 24, 2018

@author: wickm
'''
# What is the 10 001st prime number?

primelist=[1]

def primeget(n):
    testlist=[]
    for i in range (1, n+1):
        if n%i!=0:
            pass
        else:
            testlist.append(i)
            continue
    if len(testlist)==2:
        return (n)
    else:
        pass


def primego():
    i=1
    while len(primelist) in range (1, 10002):
        i=i+1
        primelist.append(primeget(i))
        if None in primelist:
            primelist.remove(None)
        else:
            print (primelist[-1])

primego()
print(primelist[-1])