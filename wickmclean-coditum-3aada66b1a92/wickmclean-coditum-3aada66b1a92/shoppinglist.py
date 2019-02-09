'''
Created on Nov 9, 2018

@author: coditum
'''
cart = []
option = ""
while option != 'exit' and option != "Exit":
    option = input('Do you want to add, remove from cart, or exit?')
    if option == 'add':
        cart.append (input('What item would you like to add?'))
    if option == 'remove':
        cart.remove (input('what item would you like to remove?'))
    if option == 'print':
        for x in range (len(cart)):
            print(cart[x])