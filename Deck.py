from Card import Card


class DeckDoNotHaveMoreCardsException(Exception):
    pass


class Deck(object):
    def __init__(self):
        self.set_of_cards = []
        self.count = 52
        self.numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
        for i in range(52):
            if (i + 1) % 13 == 1:
                self.set_of_cards.append(Card("A", 11))
            elif (i + 1) % 13 == 11:
                self.set_of_cards.append(Card("J", 10))
            elif (i + 1) % 13 == 12:
                self.set_of_cards.append(Card("Q", 10))
            elif (i + 1) % 13 == 0:
                self.set_of_cards.append(Card("K", 10))
            else:
                value = self.numbers[(i % 13) - 1]
                self.set_of_cards.append(Card(value, int(value)))

            if i < 13:
                self.set_of_cards[i].set_suits(" of Hearts")
            elif 13 <= i < 26:
                self.set_of_cards[i].set_suits(" of Diamonds")
            elif 26 <= i < 39:
                self.set_of_cards[i].set_suits(" of Clubs")
            else:
                self.set_of_cards[i].set_suits(" of Spades")

    def get_count(self):
        return self.count

    def get_card(self, index):
        return self.set_of_cards[index]

    def set_card(self, index, card):
        self.set_of_cards[index] = card

    def remove_card(self):
        if self.count == 0:
            raise DeckDoNotHaveMoreCardsException()
        else:
            self.count -= 1
            return self.set_of_cards[self.count - 1]
