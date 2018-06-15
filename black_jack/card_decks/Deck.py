"""
docstring : This class is for the deck

"""
from random import shuffle
import card_classes.card_class


class Deck(card_classes.card_class.Cards):
    deck = []

    def __init__(self):
       """
       Shuffles:keyword
       deck[52:return
       deck:var

       """
       card_classes.card_class.Cards.__init__(self)   #   initialized the class Cards from Package card_Classes

       shuffle(card_classes.card_class.car.Suits)
       """
       Docstring: Shuffling all the suits
       random:imports
       """


       for suit in card_classes.card_class.car.Suits:



            """
            Docstring: For loop to generate through the suits and ranks
            
            """
            shuffle(card_classes.card_class.car.Ranks)

            """
            
            
            Docstring: Shuffle all the ranks that are in order
            
            
            """
            for rank in card_classes.card_class.car.Ranks:

                """
                
                
                Docstring: appending the suits and ranks of class Cards to this init 
                
                """
                self.deck.append(rank +' of ' + suit)

            """
            
            Docstring: Method to shuffle all decks when all 52 of them are there
            
            """
    def shuffle_cards(self):

        shuffle(self.deck)    #  Imported from random

    """
    
    Docstring : These are the first cards dealt by the dealer
    
    """
    def deal_cards(self):

            return self.deck[:2:]

"""

docstring: Minor Error Testing by calling the values
"""

d=Deck()
d.shuffle_cards()

dealt =d.deal_cards()
print(dealt)

deal1 =str(dealt[0]).split(' ')[0]
deal2 =str(dealt[1]).split(' ')[0]
print(card_classes.card_class.car.Values[deal1]+card_classes.card_class.car.Values[deal2])



