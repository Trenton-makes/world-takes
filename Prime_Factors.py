'''
Created on Nov 28, 2018

@author: wickm
'''
#Is the number entered a prime number?


def prime_calc():
    maybe_prime = int(input('Enter a number to see if it is prime'))
    divide_list=[] 
    for num in range (1, maybe_prime+1):
        if maybe_prime % num != 0:
            True
        elif maybe_prime%num == 0:
            divide_list.append(maybe_prime)
    if len(divide_list) >= 3:
        print('Not Prime')
    else:
        print('Prime')
            
prime_calc()
