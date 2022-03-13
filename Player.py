class Player(object):
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.hand = []

    def get_points(self):
        return self.points

    def add_card(self, card):
        self.hand.append(card)
        if self.points + card.get_points() > 21:
            if card.is_an_AS():
                card.set_points(1)
            else:
                card_ = self.hand_contains_AS()
                if card_ is not None:
                    card_.set_points(1)
                    self.points -= 10
        self.points += card.get_points()

    def busted(self):
        return self.points > 21

    def get_hand(self):
        return self.hand

    def get_name(self):
        return self.name

    def is_busted(self):
        return self.points > 21

    def hand_contains_AS(self):
        for card in self.hand:
            if card.get_value() == 'A' and card.get_points() == 11:
                return card
        return None

    def player_wins(self, dealer):
        if self.busted():
            return False
        elif dealer.busted():
            return True
        else:
            return self.points > dealer.get_points()

    def player_ties(self, dealer):
        if self.busted():
            return False
        elif dealer.busted():
            return False
        else:
            return self.points == dealer.get_points()

    def player_lose(self, dealer):
        if self.busted():
            return True
        elif dealer.busted():
            return False
        else:
            return self.points < dealer.get_points()
