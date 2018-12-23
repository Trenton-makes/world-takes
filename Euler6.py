'''
Created on Dec 23, 2018

@author: wickm
'''
naturallist=[]
for i in range(1, 101):
    naturallist.append(i*i)

naturalsquare=[]
for n in range (1,101):
    naturalsquare.append(n)

sumlist=sum(naturallist)
almostthere=sum(naturalsquare)
finallythere=almostthere*almostthere


print(finallythere-sumlist)
