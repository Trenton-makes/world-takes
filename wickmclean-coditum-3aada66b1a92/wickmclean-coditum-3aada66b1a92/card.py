'''
Created on Dec 7, 2018

@author: coditum
'''
class Card:
    def __init__(self, suit, value):
        self.suit=suit
        self.value=value
    def __str__(self):
        if self.value == 11:
            temp = "Jack"
        elif self.value == 12:
            temp = "Queen"
        elif self.value == 13:
            temp = "King"
        elif self.value == 14:
            temp = "Ace"
        else: 
            temp = str(self.value)
        
        return temp + " " + self.suit
   
if __name__ == "__main__":
           
    c=Card("Clubs", 9)
    
    d=Card("Hearts", 2)
    
    e=Card("Spades", 12)
    print(e)