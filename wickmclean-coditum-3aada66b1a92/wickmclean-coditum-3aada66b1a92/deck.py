'''
Created on Dec 7, 2018

@author: coditum
'''
from card import Card
from random import randint
class Deck:
    def __init__ (self):
        self.cards=[]
        suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        for i in range (4):
            for n in range(2, 15):
                self.cards.append(Card(suits[i], n))
    def __str__ (self):
        cardlist=""
        for l in range (len(self.cards)):
            cardlist=cardlist+str(self.cards[l])+ ", "
        return cardlist
    
    def shuffle(self):
        shufflelist = []
        used=[]
        while len(self.cards)> len(used):
            n=randint(0, len(self.cards)-1)
            if n not in used:
                used.append(n)
                shufflelist.append(self.cards[n])
        self.cards = shufflelist
            
        
          
q=Deck()
q.shuffle()
deckstring = str(q)
