'''
Created on Nov 27, 2018

@author: wickm
'''
#"Find the sum of all the multiples of 3 or 5 below 1000"

list1=[]
list2=[]
for a in range (1, 1000):
    if a % 3 == 0:
        list1.append(a)
for b in range (1, 1000):
    if b % 5 == 0:
        list2.append(b)
final1=sum(list1)
final2=sum(list2)
print(final1+final2)