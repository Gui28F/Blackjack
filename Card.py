class Card(object):
    def __init__(self, value, points):
        self.value = value
        self.suits = None
        self.points = points

    def get_value(self):
        return self.value

    def set_suits(self, suit):
        self.suits = suit

    def get_points(self):
        return self.points

    def set_points(self, new_value):
        self.points = new_value

    def is_an_AS(self):
        return self.value == "A"

    def get_suits(self):
        return self.suits
