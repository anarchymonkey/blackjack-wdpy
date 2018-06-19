import card_classes.card_class
import card_decks.Deck
import Hand_class.Hands


class Chips():

    def __init__(self):

        self.total = 0
        self.bet = 0

    def win_bet(self):

        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet

        if  self.total==0:

            print("Cant place any more bets , please play later")

