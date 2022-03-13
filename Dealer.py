from random import random, randint

from blackjack_final.Deck import Deck
from blackjack_final.Player import Player


class Dealer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.deck = Deck()

    def shuffle(self):
        for i in range(self.deck.get_count() - 1):
            j = randint(0, self.deck.get_count() - 1)
            card_to_change = self.deck.get_card(i)
            self.deck.set_card(i, self.deck.get_card(j))
            self.deck.set_card(j, card_to_change)

    def give_card(self):
        return self.deck.remove_card()
