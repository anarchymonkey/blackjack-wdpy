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
    String_ranks = 'Two Three Four Five Six Seven Eight Nine King Queen Ace'.split(' ')

    def __init__(self):
        self.Suits = list(self.String_suits)
        self.Ranks = list(self.String_ranks)
        self.Values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Jack': 10, 'King': 10, 'Queen': 10, 'Ace': 11}

    def __str__(self):
        random.shuffle(self.Suits)
        random.shuffle(self.Ranks)
        return " {} of {} ".format(self.Ranks[0], self.Suits[0] )

car=Cards()
