'''
Created on Dec 14, 2018

@author: coditum
'''
def shapemain():
    x=int(input('1 for square, 2 for triangle, 3 for \
    circle, 4 for rectangle: '))
    if x == 1:
        answer=square()
    elif x==2:
        answer=triangle()
    elif x==3:
        answer=circle()
    elif x==4:
        answer=rectangle()
    else:
        print("sorry")
        return
        
    print("The area is:", answer)
def square():
    side=int(input("What is the length of the sides?"))
    area=(side*side)
    return area

def triangle():
    base=int(input("What is the length of the base?: "))
    height=int(input("What is the height?: "))
    area=.5*(base*height)
    return area

def circle():
    radius=int(input("What is the radius?: "))
    area=(3.14*radius*radius)
    return area

def rectangle():
    length=int(input("What is the length?: "))
    width=int(input("What is the width?: "))
    area=(length*width) 
    return area   

shapemain()