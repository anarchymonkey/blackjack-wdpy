"""
docstring : This class is for the deck

"""
from random import shuffle
from  card_classes.card_class import Cards



class Deck():
    deck = []

    def __init__(self):
        """
       Shuffles:keyword
       deck[52:return
       deck:var

       """

        """
       Docstring: Shuffling all the suits
       random:imports
       """

        for suit in Cards.String_suits:

            """
            Docstring: For loop to generate through the suits and ranks
            
            """

            """
            
            
            Docstring: Shuffle all the ranks that are in order
            
            
            """
            for rank in Cards.String_ranks:
                """
                
                
                Docstring: appending the suits and ranks of class Cards to this init 
                
                """
                self.deck.append(Cards(suit, rank))

            """
            
            Docstring: Method to shuffle all decks when all 52 of them are there
            
            """

    def shuffle_cards(self):
        """
        Shuffled:var
        None:return:

        """

        shuffle(self.deck)  # Imported from random

    """
    
    Docstring : These are the first cards dealt by the dealer
    
    """

    def deal_cards(self):
        """

        deck upto 2 :return:

        """
        Single_card=self.deck.pop()
        return Single_card

    def __str__(self):
        deck_comp=" "
        for card in self.deck:
            deck_comp += '\n' + card.__str__()

        return  "The deck has : " + deck_comp


"""

docstring: Minor Error Testing by calling the values
"""


#print(D)
"""
DEAL_1 = str(DEALT_CARDS[0]).split(' ')[0]
DEAL_2 = str(DEALT_CARDS[1]).split(' ')[0]
print(card_classes.card_class.car.Values[DEAL_1] + card_classes.card_class.car.Values[DEAL_2])
"""