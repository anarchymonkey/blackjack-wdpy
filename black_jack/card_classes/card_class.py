"""
docstring : Simple class for storing the whole card values , Total 53
"""
import random


class Cards():
    """
    :All the values of cards
    """
    String_suits = 'Hearts Diamonds Spades Clubs'.split(' ')
    String_ranks = '2 3 4 5 6 7 8 9 10 Jack King Queen Ace'.split(' ')
    Suits = list(String_suits)
    Ranks = list(String_ranks)
    Values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Jack': 10,
              'King': 10, 'Queen': 10, 'Ace': 11}
