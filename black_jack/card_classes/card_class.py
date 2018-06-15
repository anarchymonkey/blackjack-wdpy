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
    String_ranks = '2 3 4 5 6 7 8 9 10 Jack King Queen Ace'.split(' ')
    String_values=' Two Three Four Five Six Seven Eight Nine King Queen Ace'.split(' ')

    def __init__(self):
        self.Suits = list(self.String_suits)
        self.Ranks = list(self.String_ranks)
        self.Value = list(self.String_values)
        self.Values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Jack': 10, 'King': 10, 'Queen': 10, 'Ace': 11}

    def __str__(self):
        random.shuffle(self.Suits)
        random.shuffle(self.Value)
        return ' {} of {} '.format(self.Values[self.Value[0]] , self.Suits[0])

car=Cards()
