from time import sleep

from blackjack_final.Deck import DeckDoNotHaveMoreCardsException
from blackjack_final.Game import Game
from blackjack_final.textToSpeech import speech

speeches = ['An ', 'Good luck for the next time!']


def get_players():
    players = []
    number_of_players = input('Enter the number of players:')
    for i in range(int(number_of_players)):
        player_name = input(f"Enter the player{i + 1} name:")
        players.append(player_name)
    return players


def more_cards(game, players):
    for player in players:
        want_more_cards = 'y'
        while want_more_cards == 'y' and not game.player_is_busted(player):
            want_more_cards = input(f'Player {player} want more cards?(y/n)')
            if want_more_cards == 'y':
                game.deal_cards_to_player(True)
                print_player_hand(game, player, False)
            else:
                game.deal_cards_to_player(False)


def print_player_hand(game, player_name, no_sleep):
    hand = game.get_player_hand(player_name)
    print(player_name + ":")
    for i in range(len(hand)):
        if i == len(hand) - 1 and not no_sleep:
            speech(speeches[0] + hand[i].get_value() + hand[i].get_suits())
        print(hand[i].get_value() + hand[i].get_suits()),
    print(game.get_player_points(player_name), "points")
    if game.player_is_busted(player_name):
        print('Busted!!!')
        speech(speeches[1])


def results(game, players):
    for player in players:
        if game.player_wins(player):
            print(f'{player} wins!')
        elif game.player_ties(player):
            print(f'{player} ties!')
        elif game.player_lose(player):
            print(f'{player} lose.')


def deal_cards_dealer(game):
    game.deal_card_to_dealer()


def print_first_round(game, players):
    for player in players:
        print(player + ':')
        hand = game.get_player_hand(player)
        for hand_ in hand:
            speech(speeches[0] + hand_.get_value() + hand_.get_suits())

            print(hand_.get_value() + hand_.get_suits())
        print(game.get_player_points(player), "points")
        print()
    hand = game.get_dealer_hand()
    print(game.get_dealer_name() + ":")
    for hand_ in hand:
        sleep(2)
        print(hand_.get_value() + hand_.get_suits()),
    print(game.get_dealer_points(), "points")
    if game.dealer_busted():
        print('Busted!!!')
    print()


def print_second_round(game, players):
    for player in players:
        print(player + ':')
        hand = game.get_player_hand(player)
        for i in range(len(hand)):
            if i > 0:
                speech(speeches[0] + hand[i].get_value() + hand[i].get_suits())

            print(hand[i].get_value() + hand[i].get_suits())
        print(game.get_player_points(player), "points")
        print()
    dealer_hand(game)


def print_after_more_cards(game, players):
    print_player_hand_without_time(game, players)
    dealer_hand(game)


def dealer_hand(game):
    hand = game.get_dealer_hand()
    print(game.get_dealer_name() + ":")
    for hand_ in hand:
        print(hand_.get_value() + hand_.get_suits()),
    print(game.get_dealer_points(), "points")
    if game.dealer_busted():
        print('Busted!!!')
    print()


def print_player_hand_without_time(game, players):
    for player in players:
        print(player + ':')
        hand = game.get_player_hand(player)
        for hand_ in hand:
            print(hand_.get_value() + hand_.get_suits())
        print(game.get_player_points(player), "points")
        if game.player_is_busted(player):
            print('Busted!!!')
            speech(speeches[1])
        print()


def final_print(game, players):
    print_player_hand_without_time(game, players)
    hand = game.get_dealer_hand()
    print(game.get_dealer_name() + ":")
    for i in range(len(hand)):
        if i > 0:
            sleep(2)
        print(hand[i].get_value() + hand[i].get_suits()),
    print(game.get_dealer_points(), "points")
    if game.dealer_busted():
        print('Busted!!!')
    print()


if __name__ == '__main__':
    players = get_players()
    game = Game(players)
    try:
        game.deal_cards_to_players()
        game.deal_card_to_dealer()
        print_first_round(game, players)
        game.deal_cards_to_players()
        print_second_round(game, players)
        more_cards(game, players)
        print_after_more_cards(game, players)
        deal_cards_dealer(game)
        final_print(game, players)
        results(game, players)
    except DeckDoNotHaveMoreCardsException:
        print('Deck has no more cards.')
