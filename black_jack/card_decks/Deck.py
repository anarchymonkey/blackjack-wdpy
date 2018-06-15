"""
docstring : This class is for the deck

"""
from random import shuffle
import card_classes.card_class


class Deck(card_classes.card_class.Cards):
    deck = []

    def __init__(self):




        card_classes.card_class.Cards.__init__(self)

        shuffle(card_classes.card_class.car.Suits)
        shuffle(card_classes.card_class.car.Ranks)
        for suit in card_classes.card_class.car.Suits:
            for rank in card_classes.card_class.car.Ranks:
                self.deck.append(rank +' of ' + suit)



d=Deck()
print(d.deck)




