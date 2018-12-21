'''
Created on Nov 27, 2018

@author: wickm
'''
#"Find the sum of the even valued Fibonacci numbers from \
# 1 to four million"

def fibonacci():
    
    sumlist=[]
    list=(1,1)
    for nextnumber in range(0,4000000):
        while list[1] <= nextnumber:
            fibo=list[0]+list[1]
            list=(list[1],fibo)
            if fibo % 2 == 0:
                sumlist.append(fibo)
    print('The sum of the numbers') 
    print(sumlist)
    print('Is: ')
    print(sum(sumlist))


fibonacci()