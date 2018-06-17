"""
imports:keyword
"""
from  card_classes.card_class import Cards
from card_decks.Deck import Deck
from random import shuffle

class Hands():
    '''
    card_add,ace_Adjust:returns
    '''

    def __init__(self):
        """
        cards,values,aces:keyword
        aces ( 1 - 11) :returns
        """
        self.cards = []
        self.value = 0
        self.aces = 0

    def card_add(self,card):
        """

        cards:return:
        """
        self.cards.append(card)
        self.value += Cards.Values[card.rank]
        if card.String_ranks == 'Ace':
            self.aces += 1

    def ace_adjust(self):
        """

        aces:return:
        """

test_deck = Deck()
test_deck.shuffle_cards()
test_player = Hands()
test_player.card_add(test_deck.deal_cards())
test_player.card_add(test_deck.deal_cards())
print(test_player.value)








