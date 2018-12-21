'''
Created on Dec 20, 2018

@author: wickm
'''

def AmanAplanAcanalPanama():
    TacoCat=[]
    for i in range(111, 999):
        for n in range(111,999):
            result=i*n
            if result != int(str(result)[::-1]):
                pass
            else:
                TacoCat.append(result)
    TacoCat.sort()
    return TacoCat[-1]
palindrome=AmanAplanAcanalPanama()
print(palindrome)