#Avi Mehta


import random


class Deck(object):
    """Creates the deck"""
    
    def __init__(self):
        self.cards = [rank + suit for rank in "A23456789JQK" for suit in "CDHS"]
        temp = ["10C", "10D", "10H", "10S"]
        self.cards = self.cards + temp
        
    
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    
    """Shuffles the deck"""
        
    def shuffle(self):
        templist = self.cards
        newdeck = []
        while len(templist) > 0:
            r = random.randint(0,len(templist)-1)
            newdeck.append(templist[r])
            del templist[r]    
        self.cards = newdeck
        return newdeck
    """Deals one card if there are cards remaining in the deck"""
    
    def dealOneCard(self):
        popped = []
        if len(self.cards) > 0:
            popped.append(self.cards[0])
            return print(self.cards.pop(0))
        else:
            return print("No remaining cards in the deck")
        
deck = Deck()
for i in range(52):
    deck.dealOneCard()
deck.dealOneCard()



        

    