"""
docstring : Simple class for storing the whole card values , Total 53
"""
import random
from optparse import Values


class Cards():
    """
    :All the values of cards
    """

    String_suits = 'Hearts Diamonds Spades Clubs'.split(' ')
    String_ranks = 'Two Three Four Five Six Seven Eight Nine Ten King Queen Ace'.split(' ')
    Values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'King': 10, 'Queen': 10, 'Ace': 11}

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank


    def __str__(self):
        return self.rank + "of" + self.suit
