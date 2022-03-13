
from blackjack_final.Dealer import Dealer
from blackjack_final.Player import Player


class Game(object):
    def __init__(self, players):
        play = []
        for player_name in players:
            play.append(Player(player_name))
        self.players = play
        self.dealer = Dealer('Dealer')
        self.dealer.shuffle()
        self.current_player_index = 0
        self.max_points = 0

    def deal_cards_to_players(self):
        for player in self.players:
            card = self.dealer.give_card()
            player.add_card(card)
            if player.get_points() > self.max_points:
                self.max_points = player.get_points()

    def deal_card_to_dealer(self):
        if self.dealer.get_points() != 0:
            while self.dealer.get_points() < 17 and self.dealer.get_points() < self.max_points:
                card = self.dealer.give_card()
                self.dealer.add_card(card)
        else:
            card = self.dealer.give_card()
            self.dealer.add_card(card)
    def deal_cards_to_player(self, want_more_cards):
        player = self.players[self.current_player_index]
        if want_more_cards and not player.busted():
            card = self.dealer.give_card()
            player.add_card(card)
            if player.get_points() > self.max_points:
                self.max_points = player.get_points()
            if player.busted():
                self.next_player_index()

        else:
            # self.next_player_index()
            # player = self.players[self.current_player_index]
            # while self.has_next_player() or player.is_busted():
            self.next_player_index()
        # player = self.players[self.current_player_index]

    def get_player_by_name(self, name):
        for player in self.players:
            if player.get_name() == name:
                return player
        return None

    def first_round(self):
        self.deal_cards_to_players()
        self.deal_card_to_dealer()
        self.deal_cards_to_players()

    def next_player_index(self):
        self.current_player_index += 1

    def has_next_player(self):
        return self.current_player_index != len(self.players) - 1

    def get_player_hand(self, player_name):
        return self.get_player_by_name(player_name).get_hand()

    def get_dealer_hand(self):
        return self.dealer.get_hand()

    def get_player_points(self, player_name):
        return self.get_player_by_name(player_name).get_points()

    def get_dealer_name(self):
        return self.dealer.get_name()

    def get_dealer_points(self):
        return self.dealer.get_points()

    def player_is_busted(self, player_name):
        return self.get_player_by_name(player_name).is_busted()

    def player_wins(self, player_name):
        player = self.get_player_by_name(player_name)
        return player.player_wins(self.dealer)

    def player_ties(self, player_name):
        player = self.get_player_by_name(player_name)
        return player.player_ties(self.dealer)

    def player_lose(self, player_name):
        player = self.get_player_by_name(player_name)
        return player.player_lose(self.dealer)

    def dealer_busted(self):
        return self.dealer.busted()


"""
    def awards(self):
        for player in self.players:
            if player.player_wins(self.dealer.get_points()):
                player.aw
                """
